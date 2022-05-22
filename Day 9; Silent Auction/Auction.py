names_and_bids = {}
next_user = True
while next_user == True:
  name = input("What is your name?:\n")
  bid = int(input("What is your bid?:\n$"))

  def adding_bidder(name, bid):
    names_and_bids[name] = bid

  adding_bidder(name, bid)

  other_user = input("Are there other users who want to bid? Type 'yes' or 'no'\n").lower()
  if other_user == "no":
    next_user = False
  else:

    print(names_and_bids)

highest_bidder = ""
highest_bid = 0
for bidder in names_and_bids:
  bid_amount = names_and_bids[name]
  if names_and_bids[name] > highest_bid:
    highest_bidder = name
    highest_bid = names_and_bids[name]
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")