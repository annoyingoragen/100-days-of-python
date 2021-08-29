import random
EASY=10
HARD=5
print("Welcome to the number guessing game!")
difficultylevel=input("I'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")
number=random.randint(1,100)
remaininglives=int()
if difficultylevel=="hard":
    remaininglives=HARD
else:
    remaininglives=EASY
userreply=""
while remaininglives !=0 and userreply!=number:
    print(f"You have {remaininglives} lives left to guess the number.")
    userreply=int(input("Make a guess: "))
    if userreply<number:
        print("Too Low.")
        remaininglives-=1
        if remaininglives !=0:
            print("Guess again")
        else:
            print("You've run out of guesses, you lose.")
    if userreply>number:
        print("Too High.")
        remaininglives-=1
        if remaininglives !=0:
            print("Guess again")
        else:
            print("You've run out of guesses, you lose.")
    if userreply==number:
        print(f"You got it! The answer was {number}.")
        



