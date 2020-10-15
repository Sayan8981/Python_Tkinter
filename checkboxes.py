from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Hello coding!")
root.iconbitmap('@Inspire_2.59.xbm')

var = StringVar()

def show():
    my_label = Label(root, text= var.get()).pack()

check_btn = Checkbutton(root, text = "check this box!", variable = var, onvalue= "on", offvalue ="off")
check_btn.deselect()
check_btn.pack()


my_btn = Button(root, text= "show selection", command= show)
my_btn.pack()

root.mainloop()