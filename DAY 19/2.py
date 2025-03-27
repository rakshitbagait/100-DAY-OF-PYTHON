# edge sketch

import turtle as tt

tim = tt.Turtle()
screen = tt.Screen()
def move_forwards():
    tt.forward(10)
def move_backwards():
    tt.backward(10)
def move_clockwise():
    tt.right(5)
def move_anti_clockwise():
    tt.left(5)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="space",fun=move_forwards)
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=move_clockwise)
screen.onkey(key="d",fun=move_anti_clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()

