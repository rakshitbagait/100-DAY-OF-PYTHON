# challenge 4- Generate a Random Walk

import random, turtle as tt
timmy =tt.Turtle()
screen = tt.Screen()
screen.bgcolor("black")
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(10)
colors = ["red", "green", "blue", "yellow", "white"]
directions=[0,90,180,270]
timmy.speed("fastest")
for i in range(0,1000):
    timmy.forward(50)
    timmy.left(random.choice(directions))
    timmy.color(random.choice(colors))
   
screen.exitonclick()