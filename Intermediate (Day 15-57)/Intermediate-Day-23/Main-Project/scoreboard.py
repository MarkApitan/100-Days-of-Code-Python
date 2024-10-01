from turtle import Turtle

ALIGNMENT = 'left'
FONT = ("Courier", 24, "normal", 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.show_score()

    def show_score(self):
        self.write(f"Level = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.show_score()