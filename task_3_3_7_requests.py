import requests
from urllib.parse import urlparse
import bs4

url = input()
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
link, domains = '', set()
for a in soup.find_all('a', href=True):  # извлечь все тэги <a> с атрибутом  href
    link = a['href']  # получить ссылку из атрибута
    if not link.startswith('..'):  # если ссылка относительная - игнорируем ее
        # urlparse корректно распарсит строку, только если встретит //
        domain = urlparse(link).hostname or urlparse('//' + link).hostname
        domains.add(domain)
for item in sorted(domains):
    print(item)
