import random, turtle as tt
timmy =tt.Turtle()
screen = tt.Screen()
screen.bgcolor("black")
timmy.shape("turtle")
timmy.color("red")
colors = ["red", "green", "blue", "yellow", "white"]

for i in range(0,100):
    timmy.forward(i)
    timmy.left(90)
    timmy.color(random.choice(colors))
   
screen.exitonclick()