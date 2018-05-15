from urllib.request import urlopen
from bs4 import BeautifulSoup
import textwrap
#
# user_input = input("Please enter the webpage to scrape")
url = "https://en.wikipedia.org/wiki/Atom"
response = urlopen(url).read() # Reads (returns) webpage and saves it as a var

soup = BeautifulSoup(response, "lxml")

content = soup.find("div", class_="mw-parser-output")
# p = content.findAll("p", recursive=False)  #Find all paragraphs in main body
# title = content.findAll("span", class_="mw-headline")

together = content.findAll(["p", "title"])

filename = "output.txt"
file_handle = open(filename, "w+", encoding="utf-8")  # Open file for reading/editing

# print(title)
# for t in title:
#     print(t.string)

#write wiki output to file
# for para in p:
#     file_handle.write(t.string)
#     file_handle.write(textwrap.fill(para.text, 100))
#     file_handle.write("\n")

for f in together:
    print(f.title)
    print(f.p)
