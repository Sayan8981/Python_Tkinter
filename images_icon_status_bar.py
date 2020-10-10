from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Hello coding!")
root.iconbitmap('@Inspire_2.59.xbm')

img1 = ImageTk.PhotoImage(Image.open(os.getcwd()+"/image/Inspire_2.59.jpg"))
img2 = ImageTk.PhotoImage(Image.open(os.getcwd()+"/image/checken_leg_fry.jpg"))
img3 = ImageTk.PhotoImage(Image.open(os.getcwd()+"/image/margarita marinated flank steak tacos.jpeg"))
img4 = ImageTk.PhotoImage(Image.open(os.getcwd()+"/image/mutton_korma.jpg"))
img5 = ImageTk.PhotoImage(Image.open(os.getcwd()+"/image/Tasty grilled meat non veg food.jpeg"))

image_list = [img1, img2, img3, img4, img5]

status_bar = Label(root, text = "Image 1 of %s"%str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=2)

def forward(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(image=image_list[image_number-1])   

    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))

    if image_number == len(image_list):
         button_forward = Button(root, text=">>", state=DISABLED)

    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    label.grid(row=0, column=0, columnspan=2)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    # update status bar
    status_bar = Label(root, text = "Image %s of %s"%(str(image_number),str(len(image_list))), bd = 1, relief = SUNKEN, anchor = E)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(image=image_list[image_number-1])   

    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
         button_back = Button(root, text="<<", state=DISABLED)

    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))     

    label.grid(row=0, column=0, columnspan=2)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    # update status bar
    status_bar = Label(root, text = "Image %s of %s"%(str(image_number),str(len(image_list))), bd = 1, relief = SUNKEN, anchor = E)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text= "Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()