from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier' ,15, 'normal', 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.show_score()
    
    def show_score(self):
        self.write(f"Score = {self.score}", False, align = ALIGNMENT, font = FONT)

    def game_over (self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align = ALIGNMENT, font = FONT)
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.show_score()