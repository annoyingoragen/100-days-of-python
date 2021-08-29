# import colorgram
# colors= colorgram.extract('spot painting.jpg',30)
# colorlist=[]
# for i in range(30):
#     r=colors[i].rgb[0]
#     g=colors[i].rgb[1]
#     b=colors[i].rgb[2]
#     t=(r,g,b)
#     colorlist.append(t)

# print(colorlist)

import turtle
import random
colorlist=[ (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
print(len(colorlist))

def random_color():
    return random.choice(colorlist)

turtle.colormode(255)
tim=turtle.Turtle()
tim.pensize(5)
tim.setheading(210)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
tim.speed("fastest")
for _ in range(10):
    for _ in range(10):
        tim.pendown()
        tim.dot(20,random_color())
        tim.penup()
        tim.forward(50)
    tim.setheading(90)
    tim .penup()
    tim.forward(40)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
screen=turtle.Screen()
screen.exitonclick()