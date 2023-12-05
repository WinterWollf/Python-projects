from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", False, "center", font=("Arial", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", False, "center", font=("Arial", 16, "normal"))