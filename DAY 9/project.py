import os
print("welcome to the secret auction ")
dict={}
while(True):
    name = input("enter the name")
    bid = int(input("Enter your bid"))
    
    dict[name]=bid
    choice =(input("are there any more bidders 'yes' or 'no'")).lower()
    if choice=='no':
        break

def find_highest_bidder(bidding_dictionary):
    highest_bidder = max(bidding_dictionary ,key=bidding_dictionary.get)
    max_bid = bidding_dictionary[highest_bidder]
    print(f"The highest bidder is {highest_bidder} with bid of {max_bid}")

find_highest_bidder(dict)