from turtle  import Turtle
import os
class Scoreboard(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.score=0
        with open("data.txt",mode='r') as savedscore:
         self.highscore=int(savedscore.read())
        self.color("white")
        self.penup()
        self.goto((0,270))
        self.write(f"Score: {self.score} High Score: {self.highscore}",align="center",font=("Arial", 15, "normal"))
        self.hideturtle()
    
    def increment_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",False,align="center",font=("Arial", 15, "normal"))

    def reset(self):
        if self.score>int(self.highscore):
            self.highscore=str(self.score)        
            with open("snake\data.txt",mode='w') as savedscore:
                savedscore.write(self.highscore)
        self.score=0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",False,align="center",font=("Arial", 15, "normal"))
