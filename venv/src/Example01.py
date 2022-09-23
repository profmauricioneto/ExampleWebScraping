##############################################
#   Example of Requests
#   Code example of first sites requests with
#   get method
#############################################
import requests

URL = "https://www.google.com.br/"
my_page = requests.get(URL)

print(my_page.headers)
print(my_page.content)
print(my_page.text)
