import game_date
import art
import random
import os

os.system("cls")

LIFE = 1
points = 0

while LIFE != 0:
    pearson_a = random.randint(1, len(game_date.data))
    
    while True:
        pearson_b = random.randint(1, len(game_date.data))    
        if pearson_a != pearson_b:
            break

    print(art.logo)
    print(f"Compare A: {game_date.data[pearson_a]['name']}, {game_date.data[pearson_a]['description']}, {game_date.data[pearson_a]['country']}")
    print(art.vs)
    print(f"Against B: {game_date.data[pearson_b]['name']}, {game_date.data[pearson_b]['description']}, {game_date.data[pearson_b]['country']}")
    answer = input("Who has more followers?: Type 'A' or 'B': ").upper()

    if answer == 'A' and game_date.data[pearson_a]["follower_count"] >= game_date.data[pearson_b]["follower_count"]:
        points += 1
        os.system('cls')
        print(f"You are right! Current score: {points}")
    elif answer == 'B' and game_date.data[pearson_a]["follower_count"] <= game_date.data[pearson_b]["follower_count"]:
        points += 1
        os.system('cls')
        print(f"You are right! Current score: {points}")
    else:
        print(f"Wrong! Your score is {points}")
        break