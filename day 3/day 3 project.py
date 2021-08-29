print("Welcome to Treasure Island\n Your mission is to find the treasure")
if input("You are at a crossroad where do you want to go?left or right: ").lower() =="left":
    if input("swim or wait?").lower() =="wait":
        if input("which door?").lower() =="yellow":
            print("you win")
        else:
            print("game over")
    else:
        print("game over")
else:

    print("why game over")