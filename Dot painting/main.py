from turtle import Turtle, Screen
import color
import random

dot_size = 20
gap_size = 40

turtle = Turtle()
screen = Screen()

turtle.hideturtle()
turtle.penup()
turtle.speed(0)
screen.colormode(255)

for a in range(0, 19):
    turtle.setposition(-430, -340 + 40 * a)
    for i in range(0, 22):
        turtle.pencolor(random.choice(color.color_pallet()))
        turtle.dot(dot_size)
        turtle.forward(gap_size)

screen.exitonclick()
