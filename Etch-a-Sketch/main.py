from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()

MOVE_VALUE = 20


def move_forward():
    turtle.forward(MOVE_VALUE)


def move_backward():
    turtle.backward(MOVE_VALUE)


def turn_left():
    turtle.left(MOVE_VALUE)


def turn_right():
    turtle.right(MOVE_VALUE)


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=turtle.reset)

screen.exitonclick()
