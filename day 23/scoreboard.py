from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.goto(-250,250)
        self.color("black")
        self.hideturtle()
        self.level=1
        self.write(f"Level {self.level}",align="center",font=("Comic Sans MS", 20, "normal"))

    def level_up(self):
        self.level+=1
        self.clear()
        self.write(f"Level {self.level}",align="center",font=("Comic Sans MS", 20, "normal"))

    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Comic Sans MS", 20, "normal"))
