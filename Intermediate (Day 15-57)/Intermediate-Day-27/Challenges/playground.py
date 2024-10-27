# Create a function that take an unlimited number of arguments
# Use a loop to sum all the arguments inside the function
# def add (*args):
    # return sum(args) (easy way)
    # sum = 0
    # for arg in args:
    #     sum += arg
    # return sum

# print(add(1,2,3,4))

from tkinter import *
root = Tk()
root.geometry('500x500')
my_label = Label(text = "I am a Label", font = ("Arial", 24, "bold"))
my_label.grid(column = 0,row =0)

def button_clicked():
    my_label.config(text = input.get())

button = Button(text = "Click Me", command = button_clicked)
button.grid(column = 1,row =1)

button_two = Button(text = "Click Me", command = button_clicked)
button_two.grid(column =2,row =0)
input = Entry()
input.grid(column =3,row =2)

root.mainloop()