from tkinter import *
root = Tk()
root.title("Mile to KM Converter")
root.config(padx=20, pady=20)

def calculate():
    km = float(input.get()) * 1.60934
    answer_label.config(text = f"{km:.2f}")

input = Entry()
input.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command= calculate)
calculate_button.grid(column=1, row=2)

root.mainloop()