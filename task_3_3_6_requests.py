import re
import requests

def getHref(url: str):
    '''
    Скачивает страницу по адресу url и возвращает список ссылок
    :param url: ссылка на скачиваемую страницу
    :return: список ссылок из атрибута href
    '''
    urls = []
    try:
        response = requests.get(url, timeout=1)
        urls = re.findall(r'\bhref="(.*?(?:html|htm))">', response.text, re.MULTILINE)
    except:
        pass
    return urls


if __name__ == "__main__":
    autoTest = True # True - параметры теста берем из переменной, False - считываем из stdin
    if autoTest:
        inp = "https://stepic.org/media/attachments/lesson/24472/sample0.html\n" \
              "https://stepic.org/media/attachments/lesson/24472/sample2.html".split('\n')
    else:
        inp = input(), input()
    start_url, end_url = inp[0], inp[1]
    for url in getHref(start_url):
        if end_url in getHref(url):
            print("Yes")
            exit(0)
    print("No")
