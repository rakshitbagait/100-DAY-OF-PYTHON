# turtle 
# race

import random,turtle as tt
screen = tt.Screen()
screen.setup(width=500,height=400)
root =screen._root
root.resizable(False,False)
user_bet= screen.textinput(title="make your bet",prompt="which turtle will win the race")
color=["red","orange","green","yellow","purple"]
y_coordinates=[-100,-50,0,50,100]
all_turtles= []
for i in range(0,5):
    tim= tt.Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.color(color[i])
    tim.goto(x=-230,y=y_coordinates[i])
    all_turtles.append(tim)
    
race_on =False
if user_bet:
    race_on=True
while race_on:
    for turtle in all_turtles:
            if turtle.xcor()>230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                     print("You won")
                     
                else:
                    print(f"You lost! {winning_color} Won")
                race_on=False
            rand_distance= random.randint(0,10)
            turtle.forward(rand_distance)

screen.exitonclick()



