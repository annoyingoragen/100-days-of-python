from turtle import Turtle, xcor

class Snake:
    negative_x_limit_not_achieved=True
    positive_x_limit_not_achieved=False

    def __init__(self):
        self.snakebody=[]
        self.x_axis=0
        for _ in range(3):
            snakebody=Turtle()
            snakebody.shape("square")
            snakebody.color("white")
            snakebody.penup()
            snakebody.goto(self.x_axis,0)
            snakebody.setheading
            self.x_axis-=20
            self.snakebody.append(snakebody)
    
    def move(self):
         for i in range(len(self.snakebody)-1,0,-1):
            self.snakebody[i].goto(self.snakebody[i-1].xcor(),self.snakebody[i-1].ycor())
         self.snakebody[0].forward(20)
    
            
    def up(self):
                self.snakebody[0].setheading(90) 
            
            
    def down(self):
                self.snakebody[0].setheading(270)
              

                
    def left(self):
                self.snakebody[0].setheading(180) 

                
    def right(self):
                self.snakebody[0].setheading(0) 
