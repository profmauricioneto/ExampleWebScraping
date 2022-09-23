##############################################
#   Example of BeautifulSoup
#   Code example of first web scraper
#############################################
import requests
from colorama import Fore, Style, Back
from bs4 import BeautifulSoup
# getting site connection with get
URL = "https://www.google.com.br/"
my_page = requests.get(URL)
# parsing the html page in structure data
soup = BeautifulSoup(my_page.content, "html.parser")
# showing the data
# print(soup.prettify())

#getting some informations about content page
print(Fore.RED + Back.GREEN + "Title Page: " + Style.RESET_ALL)
print(soup.title)
print(Fore.RED + Back.GREEN + "Body Page: " + Style.RESET_ALL)
print(soup.body)

