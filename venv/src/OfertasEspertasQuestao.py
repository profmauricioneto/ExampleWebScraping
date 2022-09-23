import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.ofertaesperta.com/')

res = r.content.decode()

soup = BeautifulSoup(res, 'html.parser')

div_previous_price = soup.findAll('div', {"class":"offer-previous-price"})
div_current_price = soup.findAll('div', {"class":"offer-card-price"})

print('previous price')
for div in div_previous_price:
    price = div.find('p').text
    print(price)

print('------------------')
print('current price')
for div in div_current_price:
    # offer = div.find('div', {"class": "offer-card-price"})
    price_integer = div.find('span', {"class": "offer-card-price-integer"}).text
    price_decimal = div.find('span', {"class": "offer-card-price-decimal"})
    if (price_decimal == None):
        price_decimal = ",00"
        price = price_integer + str(price_decimal)
    else:
        price = price_integer + str(price_decimal.text)
    print(price)

# print(type(divPrice))
# print(divPrice)

# print(soup.prettify())