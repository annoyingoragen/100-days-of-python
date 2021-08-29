from turtle  import Turtle
class Paddle(Turtle):

    def __init__(self,x_pos) :
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(x_pos,0)

        
    def go_up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)
        

    def go_down(self):
        y=self.ycor()-20
        self.goto(self.xcor(),y)
        
