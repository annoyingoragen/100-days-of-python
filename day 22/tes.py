from turtle import Screen, Turtle
import turtle

turtle=turtle.Turtle()
turtle.shape("circle")
turtle.shapesize(2,2)
turtle.color("black")
turtle.penup()

screen=Screen()
for _ in range(13):
    turtle.setheading(40)
    turtle.forward(30)

screen.exitonclick()