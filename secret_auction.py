bids = {}
def highest_bidder(bidding_dic):
    highest_bid = 0
    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



continue_bidding = True


while continue_bidding:
    name = input("What is your name?: ").lower()
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any  bidders? Type 'yes or 'no'.\n ").lower()
    if should_continue == "no":
        continue_bidding = False
        highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)




