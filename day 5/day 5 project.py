import random
print("Welcome to the PyPassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',  'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

mash=[letters,numbers,symbols]
letter=int(input("How many letters would you like in your password?\n"))
symbol=int(input("How many symbols would you like in your password?\n"))
number=int(input("How many numbers would you like in your password?\n"))

total=letter+symbol+number
password=""
for pass1 in range(1,total+1):
    randlist=random.choice(mash)
    password+=random.choice(randlist)

print(password)

