from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def look_left():
    timmy.left(10)

def look_right():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=look_left)
screen.onkey(key="d", fun=look_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()