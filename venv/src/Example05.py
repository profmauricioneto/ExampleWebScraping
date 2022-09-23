##############################################
#   Example of BeautifulSoup
#   Code example of first web scraper
#   saving the data found in csv file
#############################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import csv
import os

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
    courses = soup.find('div', {'class': 'resume-content'})

    # print(courses.prettify())
    courses_vector = courses.find_all(['h4', 'h5'])
    print(courses_vector)

    taught_courses = []
    for courses_name in courses_vector:
        taught_courses.append(courses_name.text)
    print(taught_courses)

    os.mkdir('logs')
    csvFile = open('logs/courses.csv', 'w+')
    try:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(['courses'])
        for course in taught_courses:
            writer.writerow([course])
    except FileNotFoundError as e:
        print(e)
    finally:
        csvFile.close()
