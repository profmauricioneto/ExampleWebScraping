##############################################
#   Example of BeautifulSoup
#   Code example of first web scraper
#   using find and find_all methods
#############################################
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

URL = "https://maumneto.github.io/mauriciomoreira/"

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
    courses = soup.find('div', {"class": "resume-content"})

    print(courses.prettify())
    taught_course = courses.find_all(['h4', 'h5'])
    print(taught_course)

    for courses_name in taught_course:
        print(courses_name.text)




