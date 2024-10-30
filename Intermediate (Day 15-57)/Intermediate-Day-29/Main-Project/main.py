from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showinfo("Error", "Please enter all fields")
    else:
        is_yes = messagebox.askyesno(f"{str(website_entry.get()).title()}", f"These are the details entered: \nEmail: {email_entry.get()} \nPassword: {password_entry.get()}\nAre you sure you want to save?")

        if is_yes:
        # write data to the file
            with open("data.txt", "a") as file:
                file.write(f"{str(website_entry.get()).title()} | {email_entry.get()} | {password_entry.get()}\n")

            # deleting all the entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Adding the logo img
logo_img = (PhotoImage(file='logo.png'))
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

# Adding labels, entries, and buttons
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "markapitan@gmail.com")

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text='Generate Password')
generate_password_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text='Add', width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()