import re

with open("logs/text_regex.txt", "r") as my_file:
    my_text = my_file.read()
    my_ipsum_lorem = re.findall("et", my_text)
    print(my_ipsum_lorem)
