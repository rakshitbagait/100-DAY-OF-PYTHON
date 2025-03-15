# object oriented programing

import another_module

import turtle as tt
# from turtle import Turtle
timmy =tt.Turtle() 
print(timmy)
colors = ["red", "blue", "green", "yellow", "black"]

timmy.shape("turtle")
timmy.color("coral")
k=0
for i in range(10,100):
    timmy.forward(100)
    timmy.left(72)
    timmy.color(colors[k])
    if k==4:
        k=0
    else:
        k+=1


my_screen=tt.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


 