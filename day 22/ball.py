from turtle import Turtle

class Ball (Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(2,2)
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.speed(10)


    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
    
    def bounce_y(self):
        self.y_move*=-1
        
    
    def bounce_x(self):
        self.x_move*=-1

    def ball_posistion_reset(self):
        self.goto(0,0)
        self.bounce_x()