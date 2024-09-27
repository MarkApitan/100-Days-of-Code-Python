from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position = tuple):
        super().__init__()
        self.position = position
        self.create_paddle()
        
    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.color("white")
        self.goto(self.position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
