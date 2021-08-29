from turtle import Turtle, xcor

class Snake:
    negative_x_limit_not_achieved=True
    positive_x_limit_not_achieved=False

    def __init__(self):
        self.snakebody=[]
        x_axis=0
        for _ in range(3):
            snakebody=Turtle()
            snakebody.shape("square")
            snakebody.color("white")
            snakebody.penup()
            snakebody.goto(x_axis,0)
            snakebody.setheading
            x_axis-=20
            self.snakebody.append(snakebody)
        self.snakehead=self.snakebody[0]
    
    def move(self):
         for i in range(len(self.snakebody)-1,0,-1):
            self.snakebody[i].goto(self.snakebody[i-1].xcor(),self.snakebody[i-1].ycor())
         self.snakehead.forward(20)
    
    def extendsnake(self):
         snakebody=Turtle()
         snakebody.shape("square")
         snakebody.color("white")
         snakebody.penup()
         snakebody.setheading
         snakebody.goto(self.snakebody[-1].position()) 
         self.snakebody.append(snakebody)

    def up(self):
                if not (self.snakehead.heading ()== 270):
                    self.snakehead.setheading(90) 
            
            
    def down(self):
                if not (self.snakehead.heading() == 90):
                    self.snakehead.setheading(270)
              

                
    def left(self):
               
                if not (self.snakehead.heading() == 0):
                    self.snakehead.setheading(180) 

                
    def right(self):
                
                if not (self.snakehead.heading()== 180):
                    self.snakehead.setheading(0) 

    def reset(self):
             for snakeorgans  in self.snakebody:
                snakeorgans.goto(1000,1000)
             self.snakebody.clear()

             x_axis=0
             for _ in range(3):
                snakebody=Turtle()
                snakebody.shape("square")
                snakebody.color("white")
                snakebody.penup()
                snakebody.goto(x_axis,0)
                snakebody.setheading
                x_axis-=20
                self.snakebody.append(snakebody)
                self.snakehead=self.snakebody[0]
       