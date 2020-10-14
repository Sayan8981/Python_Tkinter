from tkinter import *
from PIL import ImageTk, Image
import os

from tkinter import filedialog

root = Tk()
root.title("Hello coding!")
root.iconbitmap('@Inspire_2.59.xbm')

def open_file():
    #import pdb;pdb.set_trace()
    global my_img
    root.filename = filedialog.askopenfilename(initialdir = "/home/saayan-0186/Documents/python_Tkinter/image", title = "Select A file", filetypes =(("jpg files", "*.jpg"),("All files", "*.*")))

    My_label = Label(root, text = root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image = my_img).pack()
    
my_btn = Button(root, text = "open file", command= open_file).pack()
    
root.mainloop()