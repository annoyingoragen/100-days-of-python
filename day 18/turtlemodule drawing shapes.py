from turtle import Turtle, Screen
import turtle

timmy=Turtle()
timmy.penup()
timmy.setpos(10,100)
timmy.resizemode("user")
timmy.shapesize(3, 3, 3)
timmy.pendown()
timmy.pensize(5)
timmy.color("green")
def tri():
    timmy.forward(100)
    timmy.right(120)

def square():
    timmy.forward(100)
    timmy.right(90)

def penta():
    timmy.forward(100)
    timmy.right(72)


def hexa():
    timmy.forward(100)
    timmy.right(60) 

def hepta():
    timmy.forward(100)
    timmy.right(51.42)   

    
def octa():
    timmy.forward(100)
    timmy.right(45)


def nona():
    timmy.forward(100)
    timmy.right(40)


def deca():
    timmy.forward(100)
    timmy.right(36)

for _ in range(3):
    tri()

for _ in range(4):
    timmy.color("yellow")
    square()


for _ in range(5):
    timmy.color("orange")
    penta()


for _ in range(6):
    timmy.color("pink")
    hexa()


for _ in range(7):
    timmy.color("blue")
    hepta()


for _ in range(8):
    timmy.color("brown")
    octa()


for _ in range(9):
    timmy.color("black")
    nona()


for _ in range(10):
    timmy.color("purple")
    deca()


screen= Screen()
screen.exitonclick()
