from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title ="Make your bet", prompt="Which turtle will win the race? Enter a color: " )
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []
is_onn = False

y = -100
for turtle in range (6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y)
    y+=40
    turtles.append(new_turtle)

if user_bet:
    is_onn = True

while is_onn:

    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_onn = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle was the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle was the winner.")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()