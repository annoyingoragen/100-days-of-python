from turtle import Turtle, Screen
import random
import turtle
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    rgb=(r,g,b)
    return rgb

timmy=Turtle()
direction=[0,90,180,270]
timmy.shape("circle")
timmy.pensize(9)
timmy.speed('fastest')
for _ in range(500):
    timmy.color(random_color())
    dir=random.choice(direction)
    timmy.forward(30)
    timmy.setheading(dir)



screen= Screen()
screen.exitonclick()
