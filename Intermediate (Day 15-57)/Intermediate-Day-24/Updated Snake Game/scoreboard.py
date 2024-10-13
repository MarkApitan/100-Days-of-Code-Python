from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier' ,15, 'normal', 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as self.f:
            self.high_score = int(self.f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score}       Highscore = {self.high_score}", False, align = ALIGNMENT, font = FONT)

    def reset (self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as self.f:
                self.f.write(f"{self.score}")
        self.score = 0
        self.show_score()

    def get_high_score(self):
        with open("data.txt", "r") as self.f:
            self.high_score = int(content)

    def add_score(self):
        self.score += 1
        self.show_score()