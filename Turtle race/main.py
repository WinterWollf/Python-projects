import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "yellow", "purple", "blue", "green", "orange"]
turtles = []
OFFSET = 60
winner_color = ""


def is_winning(t):
    if t.xcor() >= 250:
        global winner_color
        winner_color = turtles[i].pencolor()
        return True
    else:
        return False

for i in range(0,6):
    turtle = Turtle("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=-150 + OFFSET * i)
    turtles.append(turtle)

bet = screen.textinput(title="Make a bet", prompt="Which turtle is going to win?")

while winner_color == "":
    for i in range(0, 6):
        turtles[i].forward(random.randint(30, 40))
        if is_winning(turtles[i]):
            break

print(f"The winner is {winner_color}")
if bet == winner_color:
    print("You win!")
else:
    print("You lose!")
screen.exitonclick()
