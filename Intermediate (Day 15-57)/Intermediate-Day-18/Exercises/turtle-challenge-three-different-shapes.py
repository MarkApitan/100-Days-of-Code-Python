"""Turtle Challenge 3: Drawing Different Shapes"""
from turtle import Turtle, Screen
import random
timmy = Turtle()
colors = ["cornflower blue", "gold", "red", "green", "violet", "indigo", "dark red", "medium spring green"]
color = random.choice(colors)

for i in range (3, 11):
    color = random.choice(colors)
    timmy.color(f"{color}")
    angle = 360/i
    for num in range(i):
        timmy.forward(100)
        timmy.right(angle) 

my_screen = Screen()
my_screen.exitonclick()
