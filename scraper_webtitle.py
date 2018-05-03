from tkinter import messagebox
from urllib.request import urlopen
from bs4 import BeautifulSoup
import tkinter
import tkinter.messagebox

window = tkinter.Tk()

#Greeting text
greeting = tkinter.Label(window, text="Please enter the link of the webpage below")
greeting.pack()

#URL entry field
url = tkinter.Entry(window)
url.pack()


# parsed_url = urllib.parse.urlparse(entered_url)
def show_url_title():
    entered_url = url.get()
    response = urlopen(entered_url).read()

    soup = BeautifulSoup(response, "lxml")

    result = soup.html.head.title.string
    messagebox.showinfo("Webpage name: ", result)
#Submit button
submit = tkinter.Button(window, text="Submit", command=show_url_title)
submit.pack()

# response = urlopen(url).read()


# messagebox.showinfo("Webpage name: ", response)

window.mainloop()







# url= " https://scrapebook22.appspot.com/"
# response = urlopen(url).read()
# print(response)
#
# soup = BeautifulSoup(response, "lxml")
#
# print (soup.html.head.title.string)
#
# for link in soup.findAll("a"):
#     if link.string == "See full profile":
#         person_url = "https://scrapebook22.appspot.com" + link["href"] #Gets attrs (attribute) from link object from beautifulsoup
#         person_html = urlopen(person_url).read()
#         person_soup = BeautifulSoup(person_html, "html.parser")
#         print (person_soup.find("span", attrs={"class": "email"}).string)



