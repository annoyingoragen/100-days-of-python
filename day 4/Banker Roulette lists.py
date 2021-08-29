import random
names=input("give me everybody's name, seprarated by comma. ")

namelist=names.split(",")

# randomname=random.randint(0,len(namelist)-1)

# print(randomname)
# print(f"{namelist[randomname]} will pay the bill")

print(f"{random.choice(namelist)} will pay the bill")