from turtle import Turtle
import random

HEADING = random.uniform(0,359)


class Ball(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.resizemode("user")
        self.shapesize(0.7, 0.7)
        self.goto(0, 0)
        self.setheading(HEADING)
        self.width = width
        self.height = height
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def detect_lower_and_upper_walls_collision(self):
        if self.ycor() <= -self.height / 2 + 10 or self.ycor() >= self.height / 2 - 10:
            self.bounce_y()

    def detect_paddle_colliosion(self, l_paddle, r_paddle):
        if (self.distance(l_paddle) <= 50 or self.distance(r_paddle) <= 50) and (self.xcor() >= self.width / 2 - 38 or self.xcor() <= -self.width / 2 + 30):
            self.bounce_x()

    def detect_wall_collision(self):
        if self.xcor() <= -self.width / 2 or self.xcor() >= self.width / 2 - 5:
            return True

    def move(self, l_paddle, r_paddle):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.detect_lower_and_upper_walls_collision()
        self.detect_paddle_colliosion(l_paddle, r_paddle)
        return self.detect_wall_collision()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
