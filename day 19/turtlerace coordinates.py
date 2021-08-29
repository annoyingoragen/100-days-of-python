from turtle import Turtle, Screen, turtles
import random

screen=Screen()
screen.setup(width=500,height=500)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")
turtles=[]
colors=['red','green','yellow','orange','blue']
j=0

for i in range(5):
    tim= Turtle(shape="turtle")
    tim.color(colors[i])
    turtles.append(tim)
    turtles[i].penup()
    
    if i>=3:
        j+=1
        turtles[i].goto(x=-220, y=-j*30)
    else:
        turtles[i].goto(x=-220, y=i*30)

if user_bet:
    race_on=True

while race_on:

    for turtle in turtles:
        if turtle.xcor()>230:
            race_on=False

            if user_bet==turtle.pencolor():
                print(f"You won! winning turtle is {turtle.pencolor()}")
            else:
                print(f"You lost! winning turtle is {turtle.pencolor()}")
        turtle.forward(random.randint(0,10))

screen.exitonclick()