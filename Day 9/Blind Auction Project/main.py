# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

bids = {}
continue_auction = True
highest_bid = 0

while continue_auction:
    name = input(f"What`s your name?\n")
    bid = input(f"What is your bid?\n")
    bids[name] = int(bid)

    answer = input(f"Are there other bidder? yes/no\n")
    print("\n" * 20)
    if answer == "no":
        continue_auction = False

for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]

print(highest_bid)
