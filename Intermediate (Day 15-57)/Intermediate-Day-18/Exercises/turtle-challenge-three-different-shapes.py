"""Turtle Challenge 3: Drawing Different Shapes"""
from turtle import Turtle, Screen, colormode
import random
timmy = Turtle()
colormode(255)
def color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for i in range (3, 11):
    timmy.color(color_generator())
    angle = 360/i
    for num in range(i):
        timmy.forward(100)
        timmy.right(angle) 

my_screen = Screen()
my_screen.exitonclick()