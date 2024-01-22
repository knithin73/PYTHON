# from replit import clear
import os
bids={}

def bid(name,bid_value):
    bids[name]=bid_value
other_user=True
while other_user==True:
    os.system('clear')
    name=input("what is your name ? \n")
    bid_value=int(input("what is your bid value ? \n"))
    bid(name,bid_value)
    other_users=input("are there any other user with bid yes or no \n")
    if other_users=="no":
        other_user=False

key_max = max(bids, key = bids.get)
print(f"the winner of the bidding is {key_max}")

# highest_bid=0
# winner=""
# for names in bids:
#     bid_amount=bids[names]
#     if bid_amount>highest_bid:
#         highest_bid=bid_amount
#         winner=name

# print(f"The winner of this bidding is {winner}")
