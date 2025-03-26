import turtle as tt
tim= tt.Turtle()
screen=tt.Screen()
tim.shape("turtle")
for i in range(0,10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
screen.exitonclick()