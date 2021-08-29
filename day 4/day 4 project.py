import random
rock="""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """
paper="""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """
scissors="""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """
game_images=[rock,paper,scissors]

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
if choice<0 or choice>3 :
    print("invalid choice")
else:
    print(game_images[choice])


    computer=random.randint(0,2)
    print(game_images[computer])
    if choice==0 and computer==2:
        print("You won")
    elif choice==1 and computer==0:
        print("You won")
    elif choice==2 and computer==1:
        print("You won")
    elif choice==computer:
            print("Draw")
    else:
        print("You lose")
