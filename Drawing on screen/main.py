from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

# Ex. 1
# for i in range(0, 4):
#     turtle.forward(100)
#     turtle.right(90)

# Ex. 2
# for i in range(0, 20):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)

# Ex. 3
# screen.colormode(255)
# angle = 360
# for i in range(3, 10):
#     turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     for a in range(0, i):
#         turtle.forward(100)
#         turtle.right(angle / i)

# Ex. 4
# turtle.pensize(5)
# screen.colormode(255)
# turtle.speed(10)
# angles = [0, 90, 180, 270]
# for i in range(0, 100):
#     turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     turtle.forward(20)
#     turtle.right(random.choice(angles))

# Ex. 5
screen.colormode(255)
turtle.speed(0)
offset_angle = 5
for i in range(0, int(360 / offset_angle)):
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.circle(120)
    turtle.right(offset_angle)

screen.exitonclick()
