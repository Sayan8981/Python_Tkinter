from tkinter import *


root = Tk()
root.title("Welcome to Tkinter")
root.geometry('650x350')

# adding menu bar in root window 
# new item in menu bar labelled as 'New' 
# adding more items in the menu bar  
menu = Menu(root) 

filemenu = Menu(menu) 
menu.add_cascade(label='File', menu = filemenu)
filemenu.add_command(label='New') 
filemenu.add_command(label='Open..') 
filemenu.add_command(label='Save') 
filemenu.add_command(label='Save as') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command = root.quit) 

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu = helpmenu) 
helpmenu.add_command(label='About',)
root.config(menu=menu)

# window = Label(root, text = "Hello World!")
# window.pack()
lbl = Label(root, text = "Are you a Saayan?")
lbl.grid()

# adding Entry Field 
txt = Entry(root, width=10) 
txt.grid(column =1, row =0) 

def clicked(): 
    lbl.configure(text = "I just got clicked") 
  
# button widget with red color text 
# inside 
btn = Button(root, text = "Click me" , 
             fg = "red", command = clicked) 
  
btn.grid(column=2, row=0)

root.mainloop()