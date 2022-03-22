import requests
import requests
from bs4 import BeautifulSoup

url = 'https://journal.tinkoff.ru/guide/ad-sense/'  # url страницы
r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)
