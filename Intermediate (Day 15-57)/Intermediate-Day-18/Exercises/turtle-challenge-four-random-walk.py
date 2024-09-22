"""Turtle Challenge 4: Random Walk"""
from turtle import Turtle, Screen
import random
timmy = Turtle()
colors = ["cornflower blue", "gold", "red", "green", "violet", "indigo", "dark red", "medium spring green"]
directions = [0, 90, 180, 270]
# Change the thickness
timmy.pensize(10)
# Change the speed
timmy.speed("fast")

for i in range(100):
    color = random.choice(colors)
    timmy.color(f"{color}")
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    
my_screen = Screen()
my_screen.exitonclick()