from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jawy's Snake")
screen.tracer(0)


snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")

screen.onkey(snake.down,"Down")

screen.onkey(snake.left,"Left")

screen.onkey(snake.right,"Right")

game_on=True
while game_on:
 
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snakehead.distance(food)<14:
        food.new_food_position()
        score.increment_score()
        snake.extendsnake()

    if snake.snakehead.xcor()>280 or snake.snakehead.xcor()<-280 or snake.snakehead.ycor()>280 or snake.snakehead.ycor()<-280:
        score.gameover()
        game_on=False

    for segment in snake.snakebody[1:]:
        if snake.snakehead.distance(segment)<10:
            game_on=False
            score.gameover()
screen.exitonclick()

