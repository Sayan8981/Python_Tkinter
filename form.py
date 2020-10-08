import pandas as pd
import os
from tkinter import *

def csv(data_object):
    file_name = 'registration_form.csv'
    data = pd.DataFrame([data_object], columns = ["Name","Course","Semester","Form Number","Contact Number","Email id","Address"])

    if not os.path.isfile(file_name):
       data.to_csv(file_name, header='column_names', index = False)
    else: # else it exists so append without mentioning the header
       data.to_csv(file_name, mode='a', header=False, index = False)
 
# Function to set focus (cursor) 
def focus1(event): 
   # set focus on the course_field box 
   course_field.focus_set() 
 
# Function to set focus 
def focus2(event): 
   # set focus on the sem_field box 
   sem_field.focus_set() 
 
# Function to set focus 
def focus3(event): 
   # set focus on the form_no_field box 
   form_no_field.focus_set() 
 
# Function to set focus 
def focus4(event): 
   # set focus on the contact_no_field box 
   contact_no_field.focus_set() 
  
# Function to set focus 
def focus5(event): 
   # set focus on the email_id_field box 
   email_id_field.focus_set() 
  
# Function to set focus 
def focus6(event): 
   # set focus on the address_field box 
   address_field.focus_set() 
 
# Function for clearing the 
# contents of text entry boxes 
def clear(): 
     
    # clear the content of text entry box 
    name_field.delete(0, END) 
    course_field.delete(0, END) 
    sem_field.delete(0, END) 
    form_no_field.delete(0, END) 
    contact_no_field.delete(0, END) 
    email_id_field.delete(0, END) 
    address_field.delete(0, END) 

def insert():    
    # if user not fill any entry 
    # then print "empty input" 
    if (name_field.get() == "" and
        course_field.get() == "" and
        sem_field.get() == "" and
        form_no_field.get() == "" and
        contact_no_field.get() == "" and
        email_id_field.get() == "" and
        address_field.get() == ""): 
             
        print("empty input") 
    else: 
        data = {"Name":name_field.get(),"Course":course_field.get(),"Semester":sem_field.get(),"Form Number":form_no_field.get(),"Contact Number":contact_no_field.get(),"Email id":email_id_field.get(),"Address":address_field.get()}
        #validation = form_validation(data)
        csv([data["Name"],data["Course"],data["Semester"],data["Form Number"],data["Contact Number"],data["Email id"],data["Address"]])
        print ('%s submitted successfully'%(str(data)))

        clear()

 
# Driver code 
if __name__ == "__main__": 
     
    # create a GUI window 
    root = Tk() 

    # set the background colour of GUI window 
    root.configure(background='light green') 

    # set the title of GUI window 
    root.title("Registration form") 

    # set the configuration of GUI window 
    root.geometry("500x300") 

    # create a Form label 
    heading = Label(root, text="Form", bg="light green") 

    # create a Name label 
    name = Label(root, text="Name", bg="light green") 

    # create a Course label 
    course = Label(root, text="Course", bg="light green") 

    # create a Semester label 
    sem = Label(root, text="Semester", bg="light green") 

    # create a Form No. lable 
    form_no = Label(root, text="Form No.", bg="light green") 

    # create a Contact No. label 
    contact_no = Label(root, text="Contact No.", bg="light green") 

    # create a Email id label 
    email_id = Label(root, text="Email id", bg="light green") 

    # create a address label 
    address = Label(root, text="Address", bg="light green") 

    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    heading.grid(row=0, column=1) 
    name.grid(row=1, column=0) 
    course.grid(row=2, column=0) 
    sem.grid(row=3, column=0) 
    form_no.grid(row=4, column=0) 
    contact_no.grid(row=5, column=0) 
    email_id.grid(row=6, column=0) 
    address.grid(row=7, column=0) 

    # create a text entry box 
    # for typing the information 
    name_field = Entry(root) 
    course_field = Entry(root) 
    sem_field = Entry(root) 
    form_no_field = Entry(root) 
    contact_no_field = Entry(root) 
    email_id_field = Entry(root) 
    address_field = Entry(root) 

    # bind method of widget is used for 
    # the binding the function with the events 

    # whenever the enter key is pressed 
    # then call the focus1 function 
    name_field.bind("<Return>", focus1) 

    # whenever the enter key is pressed 
    # then call the focus2 function 
    course_field.bind("<Return>", focus2) 

    # whenever the enter key is pressed 
    # then call the focus3 function 
    sem_field.bind("<Return>", focus3) 

    # whenever the enter key is pressed 
    # then call the focus4 function 
    form_no_field.bind("<Return>", focus4) 

    # whenever the enter key is pressed 
    # then call the focus5 function 
    contact_no_field.bind("<Return>", focus5) 

    # whenever the enter key is pressed 
    # then call the focus6 function 
    email_id_field.bind("<Return>", focus6) 

    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    name_field.grid(row=1, column=1, ipadx="100") 
    course_field.grid(row=2, column=1, ipadx="100") 
    sem_field.grid(row=3, column=1, ipadx="100") 
    form_no_field.grid(row=4, column=1, ipadx="100") 
    contact_no_field.grid(row=5, column=1, ipadx="100") 
    email_id_field.grid(row=6, column=1, ipadx="100") 
    address_field.grid(row=7, column=1, ipadx="100")  

    # create a Submit Button and place into the root window 
    submit = Button(root, text="Submit", fg="Black", 
                           bg="Red", command=insert) 
    submit.grid(row=8, column=1) 

    # start the GUI 
    root.mainloop()


