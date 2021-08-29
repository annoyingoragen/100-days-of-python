print("Welcome to secret auction program")
continuebidding=True
bidders={}
while continuebidding:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: "))
    bidders[name]=bid
    continuebidding=input("Are there other bidders?: ").lower()
    if continuebidding=="y":
        continuebidding=True
    else:
        continuebidding=False
winner=int()
bidder=""
for key in bidders:
    if bidders[key]>winner:
        winner=bidders[key]
        bidder=key

print(f"winner is {bidder} with a bid of {winner}")