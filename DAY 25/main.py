import turtle
import pandas as pd

file =pd.read_csv("D:/100 Days Of Python/DAY 25/50_states.csv")
screen = turtle.Screen()
screen.title("U.S States")
image = "D:/100 Days Of Python/DAY 25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) 
game_on = True
score =0
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
guessed_states=[]
def update_score():
    global score 
    score +=1
def show_score():
    global score
    score_writer.goto(-300,270)
    score_writer.clear()
    score_writer.write(f"Score {score}",font=("Ariel",20))
while game_on:
    show_score()
    # TODO 1: CONVERT THE GUESS TO TITLE case
    guess =screen.textinput(prompt="What is name of another state?",title="Guess the states of US").title()
    # TODO 2: CHECK IF THE GUESS IS AMONG THE 50 STATES
    # TODO 3: WRITE THE GUESS ONTO THE MAP
    if guess in file["state"].values and guess not in guessed_states:
        guessed_states.append(guess)
        state=file[file["state"]==guess]
        x=int(state.x)
        y =int(state.y)
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x=x,y=y)
        marker.write(guess,font=("Ariel",10))
        update_score()
    elif guess in guessed_states:
        print("Already")
    else :
        game_on=False
        print("False")
        score_writer.goto(-250,0)
        score_writer.write(f"Your Score is :{score}",font=("Ariel",20))
        screen.ontimer(screen.bye,3000)
    if score==50:
        win = turtle.Turtle()
        win.hideturtle()
        win.penup()
        win.goto(-250,0)
        win.write(f"You win!! Your Score is :{score}",font=("Ariel",20))
        game_on=False
        screen.ontimer(screen.bye,3000)
screen.mainloop()


