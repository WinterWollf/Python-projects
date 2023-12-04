from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_chosen = ""
machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def summary():
    ammount_of_quarters = int(input("How many quarters: "))
    ammount_of_dimes = int(input("How many dimes: "))
    ammount_of_nickles = int(input("How many nickles: "))
    ammount_of_pennies = int(input("How many pennies: "))
    return float(ammount_of_quarters * 0.25 + ammount_of_dimes * 0.1 + ammount_of_nickles * 0.05 + ammount_of_pennies * 0.01)


while True:
    coffee_chosen = input(f"What would you like? {menu.get_items()}: ")

    if coffee_chosen == "report":
        machine.report()
        money_machine.report()
    elif coffee_chosen == "off":
        exit(100)
    else:
        coffee = menu.find_drink(coffee_chosen)
        if machine.is_resource_sufficient(coffee):
            money_machine.make_payment(coffee.cost)
            machine.make_coffee(coffee)
