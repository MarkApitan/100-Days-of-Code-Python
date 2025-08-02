from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        
        false_img = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-34\Main-Project\images\false.png")
        true_img = PhotoImage(file=r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-34\Main-Project\images\true.png")

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150,125,text = "Text", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0,columnspan=2, pady=50)

        self.true_button = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR, borderwidth=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, highlightthickness=0, bg=THEME_COLOR, borderwidth=0)      
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
UI = QuizInterface()