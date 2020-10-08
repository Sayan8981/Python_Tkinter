from tkinter import *

root = Tk()

mylabel = Label(root, text="Hello world!")
mylabel_name = Label(root, text="My name is Saayan")

mylabel.grid(row=0 , column=0)
mylabel_name.grid(row=1 , column=1)

#creating Buttons:

def click():
	mylabel = Label(root, text= "Look, I clicked!")
	mylabel.grid()

mynutton  = Button(root, text= "click me", padx=10,pady=10, command=click())
mynutton.grid(row=2, column=0)

root.mainloop()


