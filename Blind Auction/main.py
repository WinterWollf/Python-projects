import logo
import auction_system
from os import system

print(logo.logo)
print("Welcome in secret auction program")
others = "yes"
bidders_log = {}

while others == "yes":
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    bidders_log[name] = bid
    others = input("Are there any other bidders. Type 'yes' or 'no' ").lower()
    system('cls')

auction_system.auction(bidders_log)