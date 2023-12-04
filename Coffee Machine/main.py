from date import MENU
from date import resources

MONEY = 10
coffee_chosen = ""


def summary():
    ammount_of_quarters = int(input("How many quarters: "))
    ammount_of_dimes = int(input("How many dimes: "))
    ammount_of_nickles = int(input("How many nickles: "))
    ammount_of_pennies = int(input("How many pennies: "))
    return float(ammount_of_quarters * 0.25 + ammount_of_dimes * 0.1 + ammount_of_nickles * 0.05 + ammount_of_pennies * 0.01)


def report():
    print(f" Water: {resources['water']}\n Milk: {resources['milk']}\n Coffe: {resources['coffee']}\n Money: ${MONEY}")


def make_espresso():
    global MONEY
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    MONEY += MENU["espresso"]["cost"]
    print("Here is your espresso ☕️. Enjoy!")


def make_latte():
    global MONEY
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    MONEY += MENU["latte"]["cost"]
    print("Here is your latte ☕️. Enjoy!")


def make_cappuccino():
    global MONEY
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    MONEY += MENU["cappuccino"]["cost"]
    print("Here is your cappuccino ☕️. Enjoy!")


def can_be_purchased(coffee_type):
    if coffee_type == "off":
        exit(100)
    elif coffee_type == "report":
        report()
        return

    sum = summary()

    if coffee_type == "espresso":
        if resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"] >= 0 and resources["water"] - MENU["espresso"]["ingredients"]["water"] >= 0 and sum >= MENU["espresso"]["cost"]:
            make_espresso()
            change = sum - MENU['espresso']['cost']
            print("Here is %.2f in change." %change)
            return
    elif coffee_type == "latte":
        if resources["coffee"] - MENU["latte"]["ingredients"]["coffee"] >= 0 and resources["water"] - MENU["latte"]["ingredients"]["water"] >= 0 and resources["milk"] - MENU["latte"]["ingredients"]["milk"] >= 0 and sum >= MENU["latte"]["cost"]:
            make_latte()
            change = sum - MENU['latte']['cost']
            print("Here is %.2f in change." %change)
            return
    elif coffee_type == "cappuccino":
        if resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"] >= 0 and resources["water"] - MENU["cappuccino"]["ingredients"]["water"] >= 0 and resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"] >= 0 and sum >= MENU["cappuccino"]["cost"]:
            make_cappuccino()
            change = sum - MENU['cappuccino']['cost']
            print("Here is %.2f in change." %change)
            return

    if sum < MENU[coffee_type]["cost"]:
        print(f"Sorry that's not enough money. Money refunded ${sum}.")
    elif resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"] < 0:
        print(f"Sorry there is not enough coffee. Money refunded ${sum}.")
    elif resources["milk"] - MENU[coffee_type]["ingredients"]["milk"] < 0:
        print(f"Sorry there is not enough milk. Money refunded ${sum}.")
    elif resources["water"] - MENU[coffee_type]["ingredients"]["water"] < 0:
        print(f"Sorry there is not enough water. Money refunded ${sum}.")


while coffee_chosen != "off":
    coffee_chosen = input("What would you like? (espresso/latte/cappuccino): ")
    can_be_purchased(coffee_chosen)

report()