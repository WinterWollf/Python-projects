import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Game")

player = Player()
carlist = [CarManager()]

screen.listen()
screen.onkey(key="Up", fun=player.move)
screen.onkey(key="W", fun=player.move)
screen.onkey(key="w", fun=player.move)

game_is_on = True
helper = 0

time.sleep(3)

while game_is_on:
    time.sleep(0.1)

    for car in carlist:
        car.move()

        if player.check_colision(car) == True:
            game_is_on = False

    if helper == 6:
        carlist.append(CarManager())
        helper = 0

    helper += 1
    screen.update()
