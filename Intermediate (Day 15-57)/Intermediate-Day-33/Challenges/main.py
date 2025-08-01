from tkinter import *
import requests

def get_quote():
    #Write your code here.
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=f"{quote}")

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file= r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-33\Challenges\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-33\Challenges\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()