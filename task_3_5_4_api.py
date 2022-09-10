import requests
import json
import time
import os

STEP_ID = "101764" #идентификатор урока
#если в наборе данных встречаются эти идентификаторы, скипаем его
black_list = set(["4e96f7a9be2b4e0001003049", "525cba6f275b249fea000168", "53ee751c6361721944780200",
                  "55255e8d7261695ba22f0300"])

def get_artsy_data(artsy_token: str, id: list) -> list:
    results = []
    headers = {"X-Xapp-Token": artsy_token}
    for item in id:
        response = requests.get(f"https://api.artsy.net/api/artists/{item}", headers=headers)
        j = json.loads(response.text)
        results.append(f"{j['birthday']} {j['sortable_name'].strip()}")
    return results

def get_stepik_token(client_id: str, client_secret: str) -> str:
    # получение токена для Stepik API
    # https:// github.com/StepicOrg/Stepik-API/blob/master/examples/oauth_auth_example.py
    data = {"client_id": client_id, "client_secret": client_secret, "grant_type": 'client_credentials'}
    response = requests.post('https://stepik.org/oauth2/token/', data=data)
    return response.json().get('access_token', None)

def get_artsy_token(client_id: str, client_secret: str) -> str:
    data = {"client_id": client_id, "client_secret": client_secret}
    response = requests.post("https://api.artsy.net/api/tokens/xapp_token", data=data)
    return response.json().get('token', None)

#запрос к Stepik API на получение набора данных
def get_attempt(stepik_token: str, data: str) -> str:
    headers = {'Authorization': 'Bearer ' + stepik_token, "content-type": "application/json"}
    response = requests.post('https://stepic.org/api/attempts', data=data, headers=headers)
    return response.json()

#получение набора данных через Stepik API
def get_dataset(stepik_token: str, attempt_id: str) -> list:
    headers = {'Authorization': 'Bearer ' + stepik_token, "content-type": "application/json"}
    response = requests.get(f'https://stepic.org/api/attempts/{attempt_id}/file', headers=headers)
    return response.text.strip().split('\n')

#постим решение, возвращает wrong или correct
def submit_solution(stepik_token: str, data: str) -> str:
    headers = {'Authorization': 'Bearer ' + stepik_token, "content-type": "application/json"}
    response = requests.post('https://stepic.org/api/submissions', data=data, headers=headers)
    submission_id = response.json().get('submissions')[0]['id']
    submission_status = response.json().get('submissions')[0]['status']
    while submission_status == 'evaluation':
        response = requests.get(f'https://stepic.org/api/submissions/{submission_id}', headers=headers)
        submission_status = response.json().get('submissions')[0]['status']
        time.sleep(1)
    return submission_status

if __name__ == "__main__":
    # как получить ключи для API Stepik https://github.com/StepicOrg/Stepik-API
    # grant type выставить client credentials
    # берем ключи из переменных окружения
    stepik_client_id = os.getenv("stepik_client_id")
    stepik_client_secret = os.getenv("stepik_client_secret")
    artsy_client_id = os.getenv("artsy_client_id")
    artsy_client_secret = os.getenv("artsy_client_secret")

    stepik_token = get_stepik_token(stepik_client_id, stepik_client_secret)
    artsy_token = get_artsy_token(artsy_client_id, artsy_client_secret)

    stepik_dataset = black_list
    # пробуем получить набор данных, в котором нет ID из черного списка (black_list)
    while not set(stepik_dataset).isdisjoint(black_list):
        attempt = get_attempt(stepik_token, json.dumps({"attempt": {"step": STEP_ID}}))
        attempt_id = attempt['attempts'][0]['id']
        stepik_dataset = get_dataset(stepik_token, attempt_id)

    data = get_artsy_data(artsy_token, stepik_dataset)  # получаем список строк в формате "birthday sortable_name"

    result = ''
    for item in sorted(data):
        result += item[5:] + '\n'  # в результирующей строке будут имена разделенные \n

    submission = {"submission": {"reply": {"file": f"{result}"}, "attempt": f"{attempt_id}"}}
    result = submit_solution(stepik_token, json.dumps(submission))  # добавляем решение через Stepik API
    print(f"result is {result}")  # выводит correct