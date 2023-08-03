from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")


more_bidders = True
auction_dict = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid amount of ${highest_bid}")
    
while more_bidders == True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    
    auction_dict[name] = price

    yesORno = input("Are there any more bidders?\n").lower()
    
    if yesORno == "yes":
        clear()
    elif yesORno == "no":
        more_bidders = False
        find_highest_bidder(auction_dict)
