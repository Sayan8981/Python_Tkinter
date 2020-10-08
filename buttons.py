from tkinter import *

root = Tk()

mylabel = Label(root, text="Hello world!")
mylabel_name = Label(root, text="My name is Saayan")

mylabel.pack()
mylabel_name.pack()

#creating Buttons:

def click():
    mylabel = Label(root, text= "Look, I clicked!")
    mylabel.pack()

mybutton  = Button(root, text= "click me", padx=10,pady=10, command=click, fg="red", bg= "green")
mybutton.pack()

root.mainloop()


