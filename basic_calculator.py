from tkinter import *
from math import *

root = Tk()
root.title("Sample Calculator")

WRITE = 'w'
READ = 'r'
APPEND = 'a'

# this is for input display
display = Entry(root, bd = 5, bg = 'lightgray', fg = 'black', justify = "right", relief = "solid")
display.grid(ipadx = 40, ipady = 15, columnspan = 10)

#I am gonna make text record
fileName = "calculator.txt"
file = open(fileName, mode = APPEND)

# function for digits
def one():
    display.insert(END, 1)


def two():
    display.insert(END, 2)


def three():
    display.insert(END, 3)


def four():
    display.insert(END, 4)


def five():
    display.insert(END, 5)


def six():
    display.insert(END, 6)


def seven():
    display.insert(END, 7)


def eight():
    display.insert(END, 8)


def nine():
    display.insert(END, 9)


def zero():
    display.insert(END, 0)


def dec():
    display.insert(END, ".")

def dec():
    display.insert(END, ".")  

try:
    def add():
        s = display.get()
        if (len(s) == 0) :
            display.insert(END, "")
        else :
            display.insert(END, " + ")


    # for subtraction
    def sub():
        s = display.get()
        if (len(s) == 0) :
            display.insert(END, "")
        else :
            display.insert(END, " - ")


    # for multiplication
    def mul():
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " * ")

    # for division
    def div():
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " / ")

    #for per oparator
    def per() :
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " % ")

    # for sign and unsign
    def sign():
        #there is bug
        display.insert(END, "-")
except ValueError:
    display.insert(error)
                
# definitions of equation

try:
    def eq():
        s = display.get()
        try :
            file = open(fileName, mode = APPEND)
            file.write("\n" + s)
            file.close()
        except UnicodeEncodeError :
            pass
        if (len(s) == 0):
            display.insert(END, "")
        elif (len(s) == 1): #if user gives only single value and press = then this will fix.
            display.delete(0, END)
            display.insert(END, s)
        else :
            s = display.get()
            s = s.split()
            if (s[1] == "+"):  # for addition
                try:
                    s = float(s[0]) + float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
            elif (s[1] == "-"):  # for division
                try:
                    s = float(s[0]) - float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
            elif (s[1] == "*"):  # for multiplication
                try:
                    s = float(s[0]) * float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == "/"):  # for division
                try:
                    s = float(s[0]) / float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ZeroDivisionError:
                    display.delete(0, END)
                    display.insert(0, "Cannot devide by zero")
            elif (s[1] == '%'):   #for percentage
                try:
                    if (len(s) == 0):
                        display.insert(END, "")
                    else:
                        s = float(s[0]) / 100
                        display.delete(0, END)
                        display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)

            ################################################scientific calc###################
            elif (s[1] == '!') : #for factorial
                try:
                    s = str(factorial(int(s[0])))
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, "Give a positive integer!")

            elif (s[0] == '√') : #for underRoot
                try:
                    s = pow((float(s[1])), 1/2) #there is a problem of incoding
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, "Imaginary Number!")

            elif (s[0] == 'sin(') : #for sin
                try:
                    a = (int(s[1])) * pi / 180
                    s = sin(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'cos(') : #for cos
                try:
                    a = (int(s[1])) * pi / 180
                    s = cos(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'tan(') : #for cos
                try:
                    a = (int(s[1])) * pi / 180
                    s = tan(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'ln(') : #for ln
                try:
                    a = (float(s[1]))
                    s = log(a) #here base is e
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'log(') : #for log
                try:
                    a = (float(s[1]))
                    s = log(a, 10) #here base is e
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == '1/'):   #for inverse
                try:
                    a = float(s[1])
                    s = 1/ a;
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'e^(') : #for exponential
                try:
                    a = (float(s[1]))
                    s = exp(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)


            elif (s[1] == '^2') : #for exponential
                try:
                    a = (float(s[0]))
                    s = pow(a, 2)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == '^') : #for x raised to the power n..
                try:
                    a = (float(s[2]))
                    s = pow(float(s[0]),a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == '^') : #for x raised to the power n..
                try:
                    a = (float(s[2]))
                    s = pow(float(s[0]),a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
            try:
                file = open(fileName, mode=APPEND)
                n = " = " + str(s) + '\n' + ('-' * 50)
                file.write(n)
                file.close()
            except UnicodeEncodeError:
                pass
except ValueError :
    display.delete(0, END)
    display.insert(0, error)
except IndexError:
    display.delete(0, END)
    display.insert(0, error)  

#Define button:

# button for digits
onE = Button(root, text = '1', activebackground = 'LawnGreen'
             , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
             , command = one, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
onE.grid(row = 8, column = 0)

twO = Button(root, text = '2', activebackground = 'LawnGreen'
             , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
             , command = two, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
twO.grid(row = 8, column = 1)

threE = Button(root, text = '3', activebackground = 'LawnGreen'
               , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
               , command = three, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
threE.grid(row = 8, column = 2)

fouR = Button(root, text = '4', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = four, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
fouR.grid(row = 7, column = 0)

fivE = Button(root, text = '5', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = five, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
fivE.grid(row = 7, column = 1)

siX = Button(root, text = '6', activebackground = 'LawnGreen'
             , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
             , command = six, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
siX.grid(row = 7, column = 2)

seveN = Button(root, text = '7' , activebackground = 'LawnGreen'
               , activeforeground = 'yellow',  bd = 15, bg = 'GoldenRod'
               , command = seven, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
seveN.grid(row = 6, column = 0)

eighT = Button(root, text = '8', activebackground = 'LawnGreen'
               , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
               , command = eight, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
eighT.grid(row = 6, column = 1)

ninE = Button(root, text = '9', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = nine, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
ninE.grid(row = 6, column = 2)

zerO = Button(root,  text = '0', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = zero, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
zerO.grid(row = 9, column = 1)

deC = Button(root, text = '.', activebackground = 'LawnGreen'
             , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
             , command = dec, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
deC.grid(row = 9, column = 0)

# this button for assigning the positive and negative value....
sigN = Button(root, text = '±', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = sign, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
sigN.grid(row = 9, column = 2)

##########################################
# button for operators
# for % operator
peR = Button(root, text = '%', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = per, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
peR.grid(row = 5, column = 2)
# button for +
plus = Button(root, text = '+', activebackground = 'LawnGreen'
              , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
              , command = add, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
plus.grid(row = 8, column = 3)

# button for -
minus = Button(root, text = '-', activebackground = 'LawnGreen'
               , activeforeground = 'yellow', bd =  15, bg = 'GoldenRod'
               , command = sub, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
minus.grid(row = 7, column = 3)

# button for *
multiply = Button(root, text = '*', activebackground = 'LawnGreen'
                  , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                  , command = mul, fg = 'Indigo', justify = 'center', relief = 'groove'
                  , state = "normal")
multiply.grid(row = 6, column = 3)

# button for /
divide = Button(root, text = '/', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = div, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
divide.grid(row = 5, column = 3)


# button for = 
equal = Button(root, text = ' = ', activebackground = 'green'
               , activeforeground = 'yellow', bd = 15, bg = 'red'
               , command = eq, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
equal.grid(row = 9, column = 3)


# clear the screen
def clear():
    display.delete(0, END)


reset = Button(root, text = 'C', activebackground = 'LawnGreen'
               , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
               , command = clear, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
reset.grid(row = 5, column = 0)


# delete root value
def deleT():
    display.delete((display.index(1000)) - 1)
    #print (display.index(1000))


deletE = Button(root, text = '←', activebackground = 'LawnGreen'
                , activeforeground = 'yellow', bd = 15, bg = 'GoldenRod'
                , command = deleT, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
deletE.grid(row = 5, column = 1)

root.mainloop()


