from turtle import clear
from art import logo

print(logo)
bids = {}
shouldContinue = True

def highestBidder():
    highestBid = 0
    winner = ""
    for bidder in bids:
        bidt = bids[bidder]
        if bidt > highestBid:
            highestBid = bidt
            winner = bidder
    print(f"The winner is {winner} with bid of ${highestBid}.")

while shouldContinue:
    name = input("Name: ")
    bid = int(input("Bid: $"))
    choice = input("Anyone else. Yes or No. ").lower()

    bids[name] = bid
    if choice == "no":
        highestBidder()
        shouldContinue = False
        clear()
