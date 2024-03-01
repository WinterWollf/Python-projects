from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.player = Turtle(shape="turtle")
        self.player.penup()
        self.player.color("black")
        self.player.setheading(90)
        self.player.goto(STARTING_POSITION)

    def move(self):
        self.player.forward(MOVE_DISTANCE)

    def check_colision(self, car):
        x = abs(self.player.xcor() - car.xcor())
        y = abs(self.player.ycor() - car.ycor())

        print(f"Distance x={x}      y={y}")

        if x < 5 or y < 5:
            return True
        else:
            return False
