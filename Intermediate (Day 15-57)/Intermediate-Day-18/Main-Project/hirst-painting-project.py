"""Extract colors from an image using colorgram
note: This part of the code has been commented out because the colors have already been extracted and stored in the color_list variable."""
# import colorgram
# extract_colors = colorgram.extract('image.jpg', 30)
# color_list = []
#
# for color in extract_colors:
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     new_color = (r, g, b)
#     color_list.append(new_color)

"""Imports"""
from turtle import Turtle, Screen,colormode
import random

"""Draw the circles"""
def draw_circles():
    for i in range (10):
        timmy.pendown()
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)

"""To go to the bottom left of the screen and then go up by 50 after creating the 10 dots"""
def draw_painting():
    # get the  x and y coordinates of the bottom of the screen using turtle.pos()
    x = -212.13
    y = -212.13
    for i in range (10):
        timmy.penup()
        timmy.goto(x, y)
        draw_circles()
        y += 50

"""Create the turtle object"""
timmy = Turtle()
color_list = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]
colormode(255)
timmy.hideturtle()
timmy.speed("fastest")

draw_painting()

my_screen = Screen()
my_screen.exitonclick()