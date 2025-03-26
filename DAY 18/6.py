# spirograph

import random,turtle as tt

tim = tt.Turtle()
screen = tt.Screen()
tim.speed("fastest")

colors = ["red", "green", "blue", "yellow", "black"]
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.color(random.choice(colors))
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(5)
screen.exitonclick()

