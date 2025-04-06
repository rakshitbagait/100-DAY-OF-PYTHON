from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=600)
game_on=True
screen.tracer(0)
class Paddle(Turtle):
    def __init__(self,x,y):
        
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.5,stretch_wid=5)
        self.goto(x,y)
    def go_up(self):
            new_y=self.ycor()+50
            self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y=self.ycor()-50
        self.goto(self.xcor(),new_y)


paddle_left=Paddle(-290,0)
paddle_right=Paddle(280,0)


screen.listen()
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")

screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")


while game_on:
     screen.update()
screen.exitonclick()
