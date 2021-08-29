from turtle  import Turtle

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto((0,270))
        self.write("Score: "+str(self.score),align="center",font=("Arial", 15, "normal"))
        self.hideturtle()
    
    def increment_score(self):
        self.score+=1
        self.clear()
        self.write("Score: "+str(self.score),False,align="center",font=("Arial", 15, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!",False,align="center",font=("Arial", 15, "normal"))

