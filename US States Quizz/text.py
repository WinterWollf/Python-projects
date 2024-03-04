from turtle import Turtle


class Text(Turtle):
    def __init__(self,message, x_cor, y_cor, size = 10):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=x_cor, y=y_cor)
        self.write(f"{message}", align="center", font=("Arial", size, "normal"))
