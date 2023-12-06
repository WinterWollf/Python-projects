from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

HEIGHT = 600
WIDTH = 600
Game_is_ON = False

# Screen SetUp
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
# screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
screen.tracer(n=0)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()

# Game SetUp
left_paddle = Paddle(x_cor=-WIDTH / 2 + 18)
right_paddle = Paddle(x_cor=WIDTH / 2 - 25)
ball = Ball(width=WIDTH, height=HEIGHT)

# Key bindings
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)


while not Game_is_ON:
    screen.update()
    time.sleep(0.1)

    Game_is_ON = ball.move(left_paddle, right_paddle)


screen.exitonclick()
