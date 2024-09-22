"""Turtle Challenge 5: Draw a Spirograph"""
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

def draw_spinograph(size_of_gap):

    timmy.speed("fastest")
    for i in range (int(360/ size_of_gap)):
        timmy.color(color_generator())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading+size_of_gap)

draw_spinograph(10)
my_screen = Screen()
my_screen.exitonclick()