from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)
    
    def move(self):
        new_y = self.xcor() + 10
        new_x = self.ycor() + 10
        self.goto(new_x, new_y)