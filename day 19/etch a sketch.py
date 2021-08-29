from turtle import Turtle, Screen

tim= Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counterclock():
    tim.left(10)

def clock():
    tim.right(10)

def clearing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(key="w", fun=move_forward)

screen.onkey(key="s", fun=move_backward)

screen.onkey(key="a", fun=counterclock)

screen.onkey(key="d", fun=clock)

screen.onkey(key="c", fun=clearing)

screen.exitonclick()