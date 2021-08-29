# from turtle import Turtle, Screen
# timmy=Turtle()

# print (timmy)
# timmy.shape("turtle")
# timmy.color("red","green" )

# timmy.forward(100)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

Table= PrettyTable()

Table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
Table.add_column("Type",["Electric","Water","Fire"])
Table.align='l'


print(Table)