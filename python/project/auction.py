
bid = {}

more_bid = True

while more_bid:

    name = input("Enter the name: ")
    value = input("Enter the bid amount: $")

    bid[name] = value

    more_bid = True if input("Do you want to continue(y or n)? ").lower()=='y' else False


highest_bid = 0
highest_bidder = ''
for k,v in bid.items():
    if int(v)>highest_bid:
        highest_bidder = k
        highest_bid = int(v)

print(f"Bidders {bid}")
print(f"Highest bidder {highest_bidder} and amount {highest_bid}")