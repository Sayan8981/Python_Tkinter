from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Learn to code.....!!")

frame = LabelFrame(root, text="this is label frame.....", padx=50,pady=50)
frame.pack(padx=10, pady=10)

btn1 = Button(frame, text="Dont click here!!", command=frame.quit)
btn1.grid(row=0, column=0,pady=1)

btn2 = Button(frame, text="click here!!")
btn2.grid(row=1, column=0, pady=5)

btn_variable = IntVar() 
btn_variable.set(1)

def clicked(value):
    print ("Option %s clicked!"%str(value))
    #showwarning, showerror, askquestion, askokcancel, askyesno
    response = messagebox.askyesno("This is messagebox", "Option %s clicked!"%str(value))
    if response == 1:
    	Label(frame, text= "You clicked Yes!").grid(row=8, column=0)
    else:
        Label(frame, text= "You clicked No!").grid(row=8, column=0)	

#radio buttons:
for i in range(1,6):
    Radiobutton(frame, text="option %s"%str(i), variable=btn_variable, value=i, command=lambda: clicked(btn_variable.get())).grid(row=i+1, column=0, pady= 6+i-1)
    

root.mainloop()