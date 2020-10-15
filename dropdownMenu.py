from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Hello coding!")
root.iconbitmap('@Inspire_2.59.xbm')
root.geometry("400x400")

def show():
    my_label = Label(root, text = clicked.get()).pack()

clicked = StringVar()
options = [
    "Monday",
    "Truesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
clicked.set(options[0])
drop_menu = OptionMenu(root, clicked, *options).pack()

my_button = Button(root, text= "show selection", command=show).pack()

root.mainloop()