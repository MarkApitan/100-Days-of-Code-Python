from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier',50, 'normal', 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.show_score()
    
    def show_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, align = ALIGNMENT, font = FONT)
        self.goto(100, 200)
        self.write(self.r_score, False, align = ALIGNMENT, font = FONT)

    def game_over (self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align = ALIGNMENT, font = FONT)
    
    def r_win (self):
        self.goto(0,-50)
        self.write(f"RIGHT PLAYER WINS", False, align = ALIGNMENT, font = FONT)
    
    def l_win (self):
        self.goto(0,-50)
        self.write(f"LEFT PLAYER WINS", False, align = ALIGNMENT, font = FONT)
        
    def l_point(self):
        self.l_score += 1
        self.show_score()
    
    def r_point(self):
        self.r_score += 1
        self.show_score()