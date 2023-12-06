from turtle import Turtle
import random

HEADING = random.randint(0, 359)


class Ball(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.resizemode("user")
        self.shapesize(0.7, 0.7)
        self.goto(0, 0)
        self.speed("fastest")
        self.setheading(HEADING)
        self.width = width
        self.height = height

    def detect_lower_and_upper_walls_collision(self):
        if self.ycor() <= -self.height / 2 + 10 or self.ycor() >= self.height / 2 - 10:
            self.bounce()

    def detect_paddle_colliosion(self, l_paddle, r_paddle):
        if (self.distance(l_paddle) <= 50 or self.distance(r_paddle) <= 50) and (self.xcor() >= self.width / 2 - 38 or self.xcor() <= -self.width / 2 + 30):
            # TODO 1. Zrobić logikę jak przy bounce tylko, ze innna

    def bounce(self):
        if self.xcor() > 0:
            if self.ycor() > 0:
                self.setheading(HEADING - 90)
            else:
                self.setheading(HEADING + 90)
        elif self.xcor() < 0:
            if self.ycor() > 0:
                self.setheading(HEADING + 90)
            else:
                self.setheading(HEADING - 90)

    def detect_wall_collision(self):
        if self.xcor() <= -self.width / 2 or self.xcor() >= self.width / 2 - 5:
            return True

    def move(self, l_paddle, r_paddle):
        self.forward(10)
        self.detect_lower_and_upper_walls_collision()
        self.detect_paddle_colliosion(l_paddle, r_paddle)
        return self.detect_wall_collision()
