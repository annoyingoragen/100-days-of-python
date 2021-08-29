import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


continue_playing=True

def win():
     print(f"Your final hand: {playerscard}, final score: {playersscore}")
     print(f"computer's final hand: {computerscard}, final score: {computersscore}")  

def printscore():
    print(f"Your cards: {playerscard}, current score: {playersscore}")
    print(f"computer's first card: {computerscard[0]}")


def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(playersscore,computersscore):
    if playersscore==computersscore:
        return "DRAW"
    elif computersscore==0:
        return "You LOST, opponent has Blackjack"
    elif playersscore==0:
        playersscore=21
        return "you win with a blackjack"
    elif playersscore>21:
        return "you went over. you lost"
    elif computersscore>21:
        return "your opponent went over. you win"
    elif playersscore > computersscore:
        return "you win"
    else:
        return "you lose"

while continue_playing:
    playersscore=int()
    computersscore=int()
    playerscard=[]
    computerscard=[]
    for number in range(0,2):
        playerscard.append(random.choice(cards))
        computerscard.append(random.choice(cards))
    continue_drawing=True

    while continue_drawing:
        playersscore=calculate_score(playerscard)
        computersscore=calculate_score(computerscard)
        printscore()
        if playersscore==0 or computersscore==0 or playersscore>21:
            continue_drawing=False
        else:    
             user_draw= input("Type 'y' to get another card, type 'n'to pass: ")
             if user_draw=='y':
                playerscard.append(random.choice(cards))
                if computersscore != 0 and computersscore <17:
                    computerscard.append(random.choice(cards))
                    computersscore=calculate_score(computerscard)           
             else:
                 continue_drawing=False
    win()
    print(compare(playersscore,computersscore))
                 
                 
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':")=='y':
        continue_playing=True
    else:
        continue_playing=False
