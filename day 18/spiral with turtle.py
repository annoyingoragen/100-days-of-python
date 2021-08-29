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
timmy.shape("circle")
timmy.pensize(2)

timmy.speed('fastest')
for _ in range(int(360/5)):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading()+5)



screen= Screen()
screen.exitonclick()
