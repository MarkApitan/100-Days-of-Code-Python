from tkinter import *
import pandas as pd
import random

df = pd.read_csv(r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\data\french_words.csv")
to_learn = df.to_dict(orient='records')


def randomizer():
    random_word = random.choice(to_learn) 
    canvas.itemconfig(language_text, text='French')
    canvas.itemconfig(word_text, text=f"{random_word['French']}") 

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# Images
right_img = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\images\right.png")
wrong_img =  PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\images\wrong.png")

card_front = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\images\card_front.png")
card_back =PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\images\card_back.png")

# Canvas
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.grid(column=0,row=0,columnspan=2)

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=randomizer)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=randomizer)
right_button.grid(column=1, row=1)

randomizer()

window.mainloop()