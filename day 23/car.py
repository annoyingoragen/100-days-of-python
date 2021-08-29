COLORS=["red","orange","yellow","green","purple","blue"]
from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("square")
        self.shapesize(0.5,1)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300,random.randint(-225,225))
        self.carspeed=10

    def car_move(self):
        self.goto(self.xcor()-self.carspeed,self.ycor())
    
    def accelerate(self):
        self.carspeed+=2
    