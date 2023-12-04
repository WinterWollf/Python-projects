import game

start = input("Do you want to play a game Blackjack? Type 'y' or 'n': ").lower()

if start == 'y':
    game.run()
else:
    print("Bye. See you soon :)")
