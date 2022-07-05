#                             URL SHORTENER IN PYTHON
#                                       CSA

import pyperclip
import pyshorteners
from tkinter import *

csa = Tk()
csa.geometry("500x500")
csa.title("URL Shortener")
csa.config(bg="#549")
url = StringVar()
url_address = StringVar()


def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)


def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


python_project = Label(csa, text="Python Projects for Practice", font=(
    "Cooper Black", 20, "bold"), fg="#549")
python_project.place(x=39, y=5, height=30, width=422)

heading = Label(csa, text="URL Shortener", font=(
    "Cooper Black", 20, "bold"))
heading.place(x=85, y=45, height=50, width=330)

url_enty = Entry(csa, textvariable=url)
url_enty.place(x=85, y=135, height=50, width=330)

button_generate = Button(csa, text="Generate Short URL", font=(
    "Cooper Black", 18, "bold"), command=urlshortener)
button_generate.place(x=85, y=200, height=50, width=330)

display_url = Entry(csa, textvariable=url_address)
display_url.place(x=85, y=290, height=50, width=330)

button_copy = Button(csa, text="Copy URL", font=("Cooper Black",
                                                 16, "bold"), command=copyurl)
button_copy.place(x=85, y=355, height=50, width=330)

msg = Label(csa, text="DO LIKE AND SUBSCRIBE", font=(
    "Cooper Black", 16, "bold"))
msg.place(x=85, y=440, height=50, width=330)

csa.mainloop()
