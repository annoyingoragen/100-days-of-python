print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
per=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people=int(input("How many people to split the bill? "))

tip=bill *(per/100)

bill += tip
payment= round(bill/people, 2)

print(f"Ecah person should pay : {payment}")
