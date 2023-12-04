import random

print("Welcome to the guessing number game!")

print("Please choose difficulty 'easy' or 'hard': ")
difficulty = input("Difficulty: ").lower()

if difficulty == "hard":
    ATTEMPTS = 5
    print(f"You have got {ATTEMPTS} attempts")
else:
    ATTEMPTS = 10
    print(f"You have got {ATTEMPTS} attempts")

print("Please enter a number between 1 and 100")
guess_number = int(input("Enter a number: "))

GENERATED_NUMBER = random.randint(1,100)

while ATTEMPTS != 1:
    if guess_number == GENERATED_NUMBER:
        print("You won!")
        break
    elif guess_number < GENERATED_NUMBER:
        print("Wrong! Too low")
    else:
        print("Wrong! Too high") 
    
    ATTEMPTS -= 1
    print(f"Attempts left {ATTEMPTS}\n")
    guess_number = int(input("Enter a number: "))

print(f"Generated number was {GENERATED_NUMBER}")