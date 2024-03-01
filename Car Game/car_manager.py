import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car = Turtle()
        self.car.penup()
        self.car.shape("square")
        self.car.goto(x=280, y=self.y_position())
        self.car.shapesize(1, 2)
        self.car.color(random.choice(COLORS))
        self.car.setheading(180)

    def move(self):
        self.car.forward(STARTING_MOVE_DISTANCE)

    def y_position(self):
        return random.randint(-250, 250)

    def xcor(self):
        return self.car.xcor()

    def ycor(self):
        return self.car.ycor()
