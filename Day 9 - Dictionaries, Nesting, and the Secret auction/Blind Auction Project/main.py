
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

def max_bit (bids):
    winner = ""
    max_bit = 0
    for bit in bids:
        bid_amount = bids[bit]
        if bid_amount > max_bit:
            max_bit = bid_amount
            winner = bit
    print(f"The highest bit was: {max_bit} of {winner}")

users = {}
missing_user = True
print("Please put your name and bit")

while missing_user is True:
    name = input("Name:")
    bid = input("Bit:")
    users[name] = int(bid)
    print(users)

    left = input("Are they any missing participant left?")
    if left == "yes":
        print("\n"*1)
    elif left == "no":
        missing_user = False
        max_bit(users)
