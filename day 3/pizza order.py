print("Welcome to Python pizza deliveries!\n")
size=input("What size pizza do you want? S, M, L ")
add_pepperoni=input("Do you want pepperoni? Y/N ")
extra_cheese=input("Do you want extra cheese? Y/N ")

bill=0
if size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    bill+=15

if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra_cheese=="Y":
    bill+=1

print(f"Your bill is {bill}")
