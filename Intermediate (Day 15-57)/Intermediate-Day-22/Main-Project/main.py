from turtle import Screen, Turtle

STARTING_POSITION = (350, 0)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Turtle("square")
paddle.shapesize(stretch_wid = 5, stretch_len = 1)
paddle.penup()
paddle.color("white")
paddle.goto(STARTING_POSITION)
paddle.showturtle()

def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()