scores=input("Enter scores of students").split()
maxscore=0
for score in scores:
    score1=int(score)
    if maxscore<score1:
        maxscore=score1

print(maxscore)
