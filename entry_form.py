from tkinter import *

root = Tk()

entry = Entry(root, width=50, borderwidth=5)
entry.pack()
entry.insert(0, "Enter Name:")
#creating Buttons:

def click():
    mylabel = Label(root, text= "{} {}".format("Hello",entry.get()))
    mylabel.pack()

mybutton  = Button(root, text= "Enter your Name", padx=10,pady=10, command=click, fg="black", bg= "green")
mybutton.pack()

root.mainloop()


