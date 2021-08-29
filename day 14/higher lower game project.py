from game_data import data
import random
total_score=0
continue_playing=True
def getting_account():
    selectedindex=random.choice(data)
    return selectedindex
    
def printing_details(selectedindex):
    return (f"{selectedindex['name']} ,a {selectedindex['description']} , from {selectedindex['country']}")

def comparison(A,B,reply):
    global total_score

    if reply.lower()=='a':
        if A['follower_count']>B['follower_count']:
            total_score +=1
            print(f"You're right! Current score: {total_score}.")
            return True
        else: 
            print(f"Sorry, that's wrong. Final score: {total_score}.")
            return False
    elif reply.lower()=='b':
        if B['follower_count']>A['follower_count']:
            total_score +=1
            print(f"You're right! Current score: {total_score}.")
            return True
        else:
            print(f"Sorry, that's wrong. Final score: {total_score}.")
            return False


selectedcelebA=getting_account()
while continue_playing:
    
    print(f"Compare A: {printing_details(selectedcelebA)}")
    print("VS")
    selectedcelebB=getting_account()
    if selectedcelebA==selectedcelebB:
        selectedcelebB=getting_account()
    print(f"Compare B: {printing_details(selectedcelebB)}")
    user_reply=input("Who has more followers? Type 'A' or 'B': ").lower()
    result=comparison(selectedcelebA,selectedcelebB,user_reply)
    if result and user_reply=='b':
        selectedcelebA=selectedcelebB
    continue_playing=result
