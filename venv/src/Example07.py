##############################################
#   Example of BeautifulSoup
#   Code example of first web scraper
#   Using regex to filter the links
#############################################
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import re

URL = "https://pt.wikipedia.org/wiki/Kevin_Bacon"

try:
    my_wiki_page = urlopen(URL)
except HTTPError as e:
    print(e.code)
except URLError as e:
    print(e.reason)
else:
    soup = BeautifulSoup(my_wiki_page.read(), 'html.parser')
    div_content = soup.find('div', {'id': 'bodyContent'})
    href_regex = re.compile('^(/wiki/)((?!:).)*$')
    for link in div_content.find_all('a', href=href_regex):
        if 'href' in link.attrs:
            print(link.attrs['href'])
