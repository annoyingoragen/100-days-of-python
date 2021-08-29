from turtle import Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600,600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()
player=Player()
scoreboard=Scoreboard()

screen.onkeypress(player.move_up,"Up")

i=0
cars=[]
game_on=True
while game_on:
    if i%6==0:
        car=Car()
        cars.append(car)
    i+=1
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.car_move()
        if player.distance(car)<15:
            scoreboard.game_over()
            game_on=False
        if player.ycor()>280:
            scoreboard.level_up()
            player.position_reset()
            for car in cars:
                car.accelerate()
    # if car.xcor()<0:
    #     car.neg_x()

screen.exitonclick()
