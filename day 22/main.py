from turtle import Screen, Turtle 
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
turtle= Turtle()

screen= Screen()

screen.setup(800,600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

turtle.goto(0,310)
turtle.pencolor("white")
turtle.setheading(270)
turtle.pensize(3)
i=0
while turtle.ycor()!=-310:
    if i%2==0:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.forward(20)
    i+=1
screen.update()
turtle.color("white")
turtle.hideturtle()



l_paddle=Paddle(-370)
r_paddle=Paddle(370)
ball=Ball()
scoreboard=Scoreboard()
screen.update()

screen.listen()

screen.onkeypress(r_paddle.go_up,"Up")

screen.onkeypress(r_paddle.go_down,"Down")


screen.onkeypress(l_paddle.go_up,"w")

screen.onkeypress(l_paddle.go_down,"s")
balltime=0.1
while True:
    time.sleep(balltime)
    screen.update()
    ball.move()
    
    if  ball.ycor()>285 or ball.ycor()<-285 :
        ball.bounce_y()
        
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()
        balltime=balltime*0.9

    if ball.xcor()>380:
        ball.ball_posistion_reset()
        scoreboard.l_point()
        balltime=0.05
        
    if ball.xcor()<-380:
        ball.ball_posistion_reset()
        scoreboard.r_point()
        balltime=0.05

        
# screen.exitonclick()
while True:
    screen.update()
