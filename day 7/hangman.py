import hangman_art,random,hangman_wordlist

chosenword=random.choice(hangman_wordlist.word_list)
print(hangman_art.logo)
print(chosenword)
display=[]
for i in range(len(chosenword)):
    display.append("-")
word=""
while "-" in display and len(hangman_art.stages)!=0:
    
    
    guessletter=input("guess a letter from the word: ").lower()
    i=0
    if guessletter in chosenword:
        if guessletter not in word:
            for letter in  chosenword :
                
                if  letter== guessletter:
                    display[i]=letter
                    word=' '.join(display)
                i+=1
            print(word)
        else:
            print(f"You  have already guessed {guessletter}")
            print (word)
    else:
        print(f"you guessed {guessletter} thats not in the word You lose a life\n")
        print(hangman_art.stages.pop())

if "-" in display:
    print ("you lost")
else:
    print("you won")