print("Welcome to the love calculator!")
name1=input("What is your name?").lower()
name2=input("What is their name?").lower()
truesum=0
lovesum=0

for letter in name1:
    if letter in "true":
        truesum+=1
    if letter in "love":     
        lovesum+=1
        
for letter in name2:
 
    if letter in "true":
        truesum+=1
    if letter in "love":     
        lovesum+=1

strtrue=str(truesum)
strlove=str(lovesum)
totalsum=int(strtrue+strlove)

if totalsum < 10 or totalsum>90:
    print(f" your score is {totalsum} and you are like coke and mentos")
elif totalsum >39 and totalsum <51:
    print(f" your score is {totalsum} and you are alright together")
else:
    print(f" your score is {totalsum}")



