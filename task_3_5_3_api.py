import requests

if __name__ == "__main__":
    autoTest = True
    if autoTest:
        numbers  = [997, 902, 935, 937, 906, 971, 972, 910, 945, 918, 984, 986, 955, 924, 959]
    else:
        pass
    for item in numbers:
        url = f"http://numbersapi.com/{item}/math?json=true"
        response = requests.get(url)
        if response.status_code == 200:
            if response.json()["found"]:
                print("Interesting")
            else:
                print("Boring")
