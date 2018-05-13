from tkinter import messagebox
from urllib.request import urlopen
from bs4 import BeautifulSoup
import tkinter
import tkinter.messagebox

url = "https://scrapebook22.appspot.com/"
response = urlopen(url).read()
print(response)

soup = BeautifulSoup(response, "lxml")

print (soup.html.head.title.string)

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"] #Gets attrs (attribute) from link object from beautifulsoup
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html, "html.parser")
        print (person_soup.find("span", attrs={"class": "email"}).string)