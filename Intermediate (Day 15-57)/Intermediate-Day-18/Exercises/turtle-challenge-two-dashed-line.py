"""Draw a Dashed Line"""
from turtle import Turtle, Screen
timmy = Turtle()

for i in range(15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

my_screen = Screen()
my_screen.exitonclick()