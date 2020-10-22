from tkinter import *
from PIL import ImageTk, Image
import os,pymysql
from tkinter import messagebox

class create_db_apps:

    root = Tk()
    root.title("Form")
    root.iconbitmap('@Inspire_2.59.xbm')
    root.geometry("400x400")

    def record_window(self):    
        self.record = Tk()
        self.record.title("records")
        self.record.iconbitmap('@Inspire_2.59.xbm')
        self.record.geometry("600x600")    
    
    # set up connection of DB
    def mysql_connection(self):
        self.connection=pymysql.connect(
            user="root",
            passwd="root@123",
            host="127.0.0.1",
            db="tkinterdb",
            port=3306)
        self.cur=self.connection.cursor(pymysql.cursors.DictCursor)
        self.connection.autocommit(True)

    def clear_textbox(self):
        self.f_name.delete(0, END) 
        self.l_name.delete(0, END) 
        self.address.delete(0, END) 
        self.city.delete(0, END) 
        self.zipcode.delete(0, END)  

    def show_db_records(self):
        self.record_window()
        self.count = 0
        print_records = ''
        print ("showing all records..................")
        self.cur.execute("SELECT * from tracking")
        self.result = self.cur.fetchall()
        if self.result:
            for records in self.result:
                self.count += 1
                print_records += str(self.count) + ". " + str(records) + "\n"
            print ("\n" + print_records)
            records_label = Label(self.record, text=print_records)
            records_label.grid(row=0, column=0, columnspan=2)
    
    def submit(self):
        print("submmitted button clicked")
        try:
            if self.f_name.get() and self.l_name.get() and self.address.get() and self.city.get() and self.zipcode.get():
                self.cur.execute("INSERT INTO tracking (first_name, last_name, address, city, zipcode) values (%s,%s,%s,%s,%s)",(self.f_name.get(),self.l_name.get(),self.address.get(),self.city.get(),self.zipcode.get()))
                self.connection.close()
                self.clear_textbox()                
            else:
                print ("fields are empty ......................") 
                messagebox.showwarning("showwarning", "Warning, Every fields need to fill !")   
        except Exception as error:
            print ("exception in submmision............", type(error))

    def entry_label(self):
        self.f_name_label = Label(self.root, text="First Name")
        self.f_name_label.grid(row=0, column=0)

        self.l_name_label = Label(self.root, text="Last Name")
        self.l_name_label.grid(row=1, column=0)

        self.address_label = Label(self.root, text="Address")
        self.address_label.grid(row=2, column=0)

        self.city_label = Label(self.root, text="City")
        self.city_label.grid(row=3, column=0)

        self.zipcode_label = Label(self.root, text="Zipcode")
        self.zipcode_label.grid(row=4, column=0) 

    def entry_textbox(self):
        self.f_name = Entry(self.root, width=30)
        self.f_name.grid(row=0, column=1, padx=10)

        self.l_name = Entry(self.root, width=30)
        self.l_name.grid(row=1, column=1)

        self.address = Entry(self.root, width=30)
        self.address.grid(row=2, column=1)

        self.city = Entry(self.root, width=30)
        self.city.grid(row=3, column=1,)
 
        self.zipcode = Entry(self.root, width=30)
        self.zipcode.grid(row=4, column=1)

    def click_to_buttons(self):
        self.entry_label()
        self.entry_textbox()
        self.mysql_connection()
        self.submit_btn = Button(self.root, text="Add record to database", command=self.submit)
        self.submit_btn.grid(row=6, column=0, columnspan=2, padx=15, pady=10, ipadx=100) 
        
    def show_records(self):    
        self.show_record_btn = Button(self.root, text="Show records", command=self.show_db_records)
        self.show_record_btn.grid(row=8, column=0, columnspan=2, padx=15, pady=10, ipadx=100)        
        
    def main(self):
        self.click_to_buttons()
        self.show_records()
        self.root.mainloop()                         
    
if __name__ == '__main__':
    create_db_apps().main()
    