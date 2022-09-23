##############################################
#   Example of BeautifulSoup
#   Code example of first web scraper
#
#############################################
import datetime

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import random
import re

# URL = "https://pt.wikipedia.org/wiki/Kevin_Bacon"
random.seed(10)


def get_links(article_url):
    try:
        page = "http://pt.wikipedia.org{}".format(article_url)
        print(page)
        my_wiki_page = urlopen(page)
    except HTTPError as e:
        print(e.code)
    except URLError as e:
        print(e.reason)
    else:
        soup = BeautifulSoup(my_wiki_page, "html.parser")
        div_content = soup.find('div', {'id': 'bodyContent'})
        href_regex = re.compile('^(/wiki/)((?!:).)*$')
        links_anchors = soup.find(div_content.find_all('a'), href=href_regex)
    return links_anchors


wiki_links = []
wiki_links = get_links('/wiki/Kevin_Bacon')
print(wiki_links)
# while len(wiki_links) > 0:
#     new_article = wiki_links[random.randint(0, len(wiki_links) - 1)].attrs['href']
#     print(new_article)
#     links = get_links(new_article)
