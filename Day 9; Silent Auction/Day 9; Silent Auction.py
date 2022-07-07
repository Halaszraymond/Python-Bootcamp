# Day 9: Silent Auction

# from replit import clear

from art import logo
print(logo)

names_and_bids = {}
next_user = True

# Onderstaand code loopen totdat er aangegeven wordt dat er geen extra mensen meer meedoen
while next_user:
    name = input("What is your name?:\n")
    bid = int(input("What is your bid?:\n$"))

    names_and_bids[name] = bid
    other_user = input("Are there other users who want to bid? Type 'yes' or 'no'\n").lower()
    if other_user == "no":
        next_user = False
    # else:
    # clear()

# Bepalen wie het hoogste bod heeft
highest_bidder = ""
highest_bid = 0
for bidder in names_and_bids:
    if names_and_bids[bidder] > highest_bid:
        highest_bidder = bidder
        highest_bid = names_and_bids[bidder]
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

