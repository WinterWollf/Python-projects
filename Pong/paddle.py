from turtle import Turtle

MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, x_cor=0, y_cor=0):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color("white")
        self.shape("square")
        self.resizemode("user")
        self.shapesize(0.5, 5)
        self.goto(x_cor, y_cor)
        self.speed("fastest")


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)