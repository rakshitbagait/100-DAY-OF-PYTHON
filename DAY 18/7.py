import turtle as tt

t = tt.Turtle()
t.pensize(2)
t.speed(0)

def draw():
    for i in range(4):
        t.forward(40)
        t.right(90)

    t.forward(40)

for i in range(8):
    t.penup()
    t.goto(0, 40*i)
    t.pendown()
    for x in range(8):
        if(x+i)%2==0:
            color="black"
        else:
            color ="white"
        t.fillcolor(color)
        t.begin_fill()
        draw()
        t.end_fill()

t.hideturtle()
tt.done()