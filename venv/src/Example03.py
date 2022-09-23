##############################################
#   Example of BeautifulSoup
#   Code example of first web scraper
#   with exception treatment
#############################################
from colorama import Fore, Style, Back
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# getting site connection with get
URL = "https://maumneto.github.io/mauriciomoreira/"

try:
    my_page = urlopen(URL)
except HTTPError as e:
    print('HTTP Error')
    print(e.code)
except URLError as e:
    print("Server not found")
    print(e.reason)
else:
    print(Fore.BLACK + Back.GREEN + "It Work " + Style.RESET_ALL)
    # parsing the html page in structure data
    soup = BeautifulSoup(my_page.read(), "html.parser")
    # showing the data
    print(soup.prettify())
