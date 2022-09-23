from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = "https://www.google.com.br/"
my_page = urlopen(URL)

soup = BeautifulSoup(my_page.read(), "html.parser")

print(soup.prettify())
