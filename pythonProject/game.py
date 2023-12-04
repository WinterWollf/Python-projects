import random
import logo
from deck import deck


def display(p_deck, c_deck):
    """Displaying current cards decks and scores values"""
    print(f"Your cards: {p_deck}, current score: {score(p_deck)}")
    print(f"Computer's first card: {c_deck[0]}")
    if score(p_deck) > 21:
        summary(p_deck, c_deck)
    else:
        return input(f"Type 'y' to get another card, type 'n' to pass: ").lower()


def run():
    """Main game"""
    print(logo.art)
    player_deck = starters()
    computer_deck = starters()
    answer = display(player_deck, computer_deck)

    while score(computer_deck) < 17:
        computer_deck.append(drawing())

    while score(player_deck) <= 21:
        if answer == 'y':
            player_deck.append(drawing())
            answer = display(player_deck, computer_deck)
        else:
            summary(player_deck, computer_deck)
            break


def drawing():
    """Mechanic of randomly drawing a card"""
    pulled = random.choice(list(deck.values()))
    template = [1, 11]

    if pulled == template:
        return random.choice(pulled)
    else:
        return pulled


def starters():
    """Create starter pack of cards"""
    starter_pack = []
    for i in range(0, 2):
        starter_pack.append(drawing())
    return starter_pack


def score(deck_score):
    """Return summary score for given deck of cards"""
    sum = 0
    for card in deck_score:
        sum += card
    return sum


def summary(p_deck, c_deck):
    """Main game rules"""
    print(f"Your final hand: {p_deck}, final score: {score(p_deck)}")
    print(f"Computer's final hand: {c_deck}, final score: {score(c_deck)}")

    if score(p_deck) == score(c_deck):
        print("Draw 🙃")
    elif score(p_deck) == 21:
        print("Win with a Blackjack 😎")
    elif score(p_deck) > 21:
        print("You went over. You lose 😭")
    elif score(c_deck) > 21:
        print("Opponent went over. You win 😁")
    elif 21 - score(p_deck) < 21 - score(c_deck):
        print("You win 😃")
    else:
        print("You lose 😤")