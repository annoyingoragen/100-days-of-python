import turtle,pandas

states_data=pandas.read_csv("50_states.csv")



screen=turtle.Screen()
screen.title=("USA state quiz")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape((image))

guessed_states=[]
unguessed_states=[]
while len(guessed_states)<50:
   answer= turtle.textinput(f"{len(guessed_states)}/50 states","Guess the states of USA").title()
   state_coordinates=states_data[states_data['state']==answer]
   if answer=="Exit":
       for state in states_data['state'].to_list():
           if not(state in guessed_states):
               unguessed_states.append(state)

       unguessed_states_dataframe={
           "unguessed states":unguessed_states
       }
       df=pandas.DataFrame(unguessed_states_dataframe)
       df.to_csv("unguessed states.csv")
       break
   if not state_coordinates.empty:
       tim=turtle.Turtle()
       tim.hideturtle()
       tim.penup()
       x = int(state_coordinates.x)
       y = int(state_coordinates.y)
       guessed_states.append(answer)
       tim.goto(x,y)
       state_name=state_coordinates.state.item()
       tim.write(state_name)



