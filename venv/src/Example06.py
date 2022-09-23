##############################################
#   Example of BeautifulSoup
#   Code example of first web scraper
#   Filter all links of Kevin Bacon's wiki
#############################################
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

URL = "https://pt.wikipedia.org/wiki/Kevin_Bacon"

my_page = urlopen(URL)
soup = BeautifulSoup(my_page.read(), 'html.parser')
for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
