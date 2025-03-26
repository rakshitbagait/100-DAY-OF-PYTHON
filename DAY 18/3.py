#drawing multiple shapes

import turtle as tt
screen = tt.Screen()
tim = tt.Turtle()

tim.shape("turtle")

tom = tt.Turtle()
tom.shape("circle")
tom.setx(100)
tom.forward(10)
for i in range(0,5):
    tim.forward(100)
    tim.right(90)
    tom.forward(100)
    tom.right(72)
screen.exitonclick()
