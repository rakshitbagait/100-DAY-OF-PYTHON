import turtle as tt
timmy =tt.Turtle()
screen = tt.Screen()
timmy.shape("turtle")
timmy.color("red")
for i in range(0,4):
    timmy.forward(100)
    timmy.left(90)

   
screen.exitonclick()