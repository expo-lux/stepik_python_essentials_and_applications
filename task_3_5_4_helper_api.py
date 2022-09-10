import time
import requests
import json
import os
from plumbum.cmd import sort, comm, uniq

STEP_ID = "101764"

black_list = set(["4e96f7a9be2b4e0001003049", "525cba6f275b249fea000168", "53ee751c6361721944780200",
              "55255e8d7261695ba22f0300"])


def get_artsy_data(artsy_token: str, id: list) -> list:
    results = []
    headers = {"X-Xapp-Token": artsy_token}
    for item in id:
        response = requests.get(f"https://api.artsy.net/api/artists/{item}", headers=headers)
        # response.encoding = 'utf-8'
        j = json.loads(response.text)
        results.append(f"{j['birthday']} {j['sortable_name'].strip()}")
    return results

def get_black_list(artsy_token: str, id: list):
    results = []
    headers = {"X-Xapp-Token": artsy_token}
    for item in id:
        response = requests.get(f"https://api.artsy.net/api/artists/{item}", headers=headers)
        # response.encoding = 'utf-8'
        j = json.loads(response.text)
        results.append(f"{item} {j['birthday']} {j['sortable_name'].strip()}")
    return results

def get_stepik_token(client_id: str, client_secret: str) -> str:
    # получение токена
    # https:// github.com/StepicOrg/Stepik-API/blob/master/examples/oauth_auth_example.py
    data = {"client_id": client_id, "client_secret": client_secret, "grant_type": 'client_credentials'}
    response = requests.post('https://stepik.org/oauth2/token/', data=data)
    return response.json().get('access_token', None)
    # if not token:
    #     print('Unable to authorize with provided credentials')
    #     exit(1)
    # return token




def get_artsy_token(client_id: str, client_secret: str) -> str:
    data = {"client_id": client_id, "client_secret": client_secret}
    response = requests.post("https://api.artsy.net/api/tokens/xapp_token", data=data)
    return response.json().get('token', None)
    # print(curlify.to_curl(r.request))
    # разбираем ответ сервера
    # j = json.loads(r.text)
    # # достаем токен
    # return j["token"]


def get_attempt(stepik_token: str, data: str) -> str:
    headers = {'Authorization': 'Bearer ' + stepik_token, "content-type": "application/json"}
    response = requests.post('https://stepic.org/api/attempts', data=data, headers=headers)
    return response.json()


def get_dataset(stepik_token: str, attempt_id: str) -> list:
    headers = {'Authorization': 'Bearer ' + stepik_token, "content-type": "application/json"}
    response = requests.get(f'https://stepic.org/api/attempts/{attempt_id}/file', headers=headers)
    return response.text.strip().split('\n')


def submit_solution(stepik_token: str, data: str) -> str:
    headers = {'Authorization': 'Bearer ' + stepik_token, "content-type": "application/json"}
    response = requests.post('https://stepic.org/api/submissions', data=data, headers=headers)
    submission_id = response.json().get('submissions')[0]['id']
    print(f"submission ID is {submission_id}")
    submission_status = response.json().get('submissions')[0]['status']
    while submission_status == 'evaluation':
        response = requests.get(f'https://stepic.org/api/submissions/{submission_id}', headers=headers)
        submission_status = response.json().get('submissions')[0]['status']
        time.sleep(1)
    return submission_status


def submit_solutionL(stepik_token: str, data: str) -> str:
    headers = {'Authorization': 'Bearer ' + stepik_token, "content-type": "application/json"}
    response = requests.post('http://localhost:8080', data=data, headers=headers)


if __name__ == '__main__':
    # как получить ключи для API Stepik https://github.com/StepicOrg/Stepik-API
    # grant type выставить client credentials
    stepik_client_id = os.getenv("stepik_client_id")
    stepik_client_secret = os.getenv("stepik_client_secret")
    artsy_client_id = os.getenv("artsy_client_id")
    artsy_client_secret = os.getenv("artsy_client_secret")

    # if not (stepik_client_secret and stepik_client_id and artsy_client_secret and artsy_client_id):
    #     print('Environment variable is note defined')
    #     exit(1)

    stepik_token = get_stepik_token(stepik_client_id, stepik_client_secret)
    artsy_token = get_artsy_token(artsy_client_id, artsy_client_secret)

    data = get_black_list(artsy_token, list(black_list))
    for item in data:
        print(item)

    for k in range(40):
        attempt = get_attempt(stepik_token, json.dumps({"attempt": {"step": STEP_ID}}))
        attempt_id = attempt['attempts'][0]['id']
        stepik_dataset = get_dataset(stepik_token, attempt_id)

        try:
            data = get_artsy_data(artsy_token, stepik_dataset)
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            continue
        result = ''
        for item in sorted(data):
            result += item[5:] + '\n'
            print(item)
        # result += '\n'
        print(f"{len(data)} overall items")

        time.sleep(10)
        submission = {"submission": {"reply": {"file": f"{result}"}, "attempt": f"{attempt_id}"}}
        submit_solutionL(stepik_token, json.dumps(submission))
        result = submit_solution(stepik_token, json.dumps(submission))
        print(f"result is {result}")
        if result == "wrong":
            with open("task_3_5_4_api_wrong.txt", "a") as f:
                for item in stepik_dataset:
                    f.write(f"{item}\n")
        elif result == "correct":
            with open("task_3_5_4_api_correct.txt", "a") as f:
                for item in stepik_dataset:
                    f.write(f"{item}\n")

    (sort["task_3_5_4_api_wrong.txt"] | uniq > "wrong")()
    (sort["task_3_5_4_api_correct.txt"] | uniq > "correct")()
    (comm["-23", "wrong", "correct"] > "dataset_24476_4.txt")()
