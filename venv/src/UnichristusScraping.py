from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

URL = "https://unichristus.edu.br/"

try:
    my_page = urlopen(URL)
except HTTPError as e:
    print("HTTP Error!")
    print(e)
except URLError as e:
    print("Server not found")
    print(e)
else:
    soup = BeautifulSoup(my_page, "html.parser")
    news = soup.find('div', {"class": "wgt-outras-noticias"})

    new_events = news.find_all(['a'])
    print(new_events)

    for event in new_events:
        print(event.get_text())




