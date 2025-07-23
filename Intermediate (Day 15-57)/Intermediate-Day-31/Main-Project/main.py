from tkinter import *
import pandas as pd
import random

# Removes the current word from the list, saves progress, and shows the next card
def remove_word():
    to_learn.remove(current_word)
    pd.DataFrame(to_learn).to_csv(file_path, index=False)  # Save updated list to CSV
    next_card()

# Flips the card to show the English translation
def show_answer():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_text, text='English', fill="white")
    canvas.itemconfig(word_text, text=f"{current_word['English']}", fill="white")

# Shows a new random French word and sets up the timer to flip the card
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)  # Cancel previous timer
    current_word = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language_text, text='French', fill="black")
    canvas.itemconfig(word_text, text=f"{current_word['French']}", fill="black")
    flip_timer = window.after(3000, func=show_answer)  # Flip after 3 seconds

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=show_answer)  # Initial timer

# Load words to learn from CSV, or fallback to original list if not found
file_path = r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\data\words_to_learn.csv"
try:
    df = pd.read_csv(file_path)
    to_learn = df.to_dict(orient='records')
except FileNotFoundError:
    df = pd.read_csv(r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\data\french_words.csv")
    to_learn = df.to_dict(orient='records')
current_word = {}

# Load images for cards and buttons
right_img = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\images\right.png")
wrong_img = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\images\wrong.png")
card_front = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\images\card_front.png")
card_back = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-31\Main-Project\images\card_back.png")

# Set up the flashcard canvas and text
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons for marking wrong/right answers
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=remove_word)
right_button.grid(column=1, row=1)

# Start with the first car
next_card()  

window.mainloop() 