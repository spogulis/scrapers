from urllib.request import urlopen
from bs4 import BeautifulSoup
#
# user_input = input("Please enter the webpage to scrape")
url = "https://en.wikipedia.org/wiki/Atom"
response = urlopen(url).read() # Reads (returns) webpage and saves it as a var

soup = BeautifulSoup(response, "lxml")

content = soup.find("div", class_="mw-parser-output")
p = content.findAll("p", recursive=False)
# for p in p:
#     print(p.text)

filename = "output.txt"
file_handle = open(filename, "w+", encoding="utf-8")  # Open file for reading/editing
#write wiki output to file
for p in p:
    file_handle.write(p.text)



# print(table)
# print(soup.html.body.table['class':'infobox'])