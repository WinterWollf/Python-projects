import random
import stages
import dictionary

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(dictionary.word_list)
health = 6
game_status = True
test_list = []

for letter in chosen_word:
    test_list.append("_")

print(stages.logo + "\n")

# Testing reason only! #
print(f"Chosen word is: {chosen_word}")

while '_' in test_list:
    guess = (input("Guess a letter: ")).lower()
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            if guess in test_list and guess != '_':
                print(f"\nYou have already guessed {guess}")
            else:
                test_list[i] = guess
    if guess not in test_list:
        print(stages.stages[health])
        health -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life. Remaining lives: {health}")
    print(test_list)
    if health < 0:
        game_status = False
        break

if not game_status:
    print("\nLose")
else:
    print("\nWin")