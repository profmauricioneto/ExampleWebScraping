from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import requests

URL = "https://www.ofertaesperta.com/"

html = requests.get(URL).content.decode()
soup = BeautifulSoup(html, 'html.parser')
div_previous_price = soup.find_all('div', {"class": "offer-previous-price"})
div_current_price = soup.find_all('div', {"class": "offer-card-price"})
print('previous price')
for div in div_previous_price:
    price = div.find('p').text
    print(price)
