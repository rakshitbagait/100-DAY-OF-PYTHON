from turtle import Turtle, Screen
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(height=500,width=700)
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
paddle_left=Paddle(-340,0)
paddle_right=Paddle(330,0)

class Ball(Turtle):
    def __init__(self):
          super().__init__()
        
          self.penup()
          self.shape("circle")
          self.color("white")
          self.x_move =0.1
          self.y_move=0.1
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_wall(self):
         self.y_move *=-1
    def bouce_paddel(self):
         self.x_move *=-1
    def ball_refresh(self):
        self.goto(0,0)
        self.y_move*=-1
        self.x_move *=-1        
ball = Ball()
screen.listen()
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")

screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")

class Scoreboard(Turtle):
    def __init__(self):
          super().__init__()
          self.hideturtle()
          self.penup()
          self.color("white")
          self.left_score =0
          self.right_score=0
          self.update_score()
    def update_score(self):
          self.clear()
          self.goto(-100,150)
          self.write(self.left_score,align="center",font=("Courier",80,"normal"))
          self.goto(100,150)
          self.write(self.right_score,align="center",font=("Courier",80,"normal"))
    def r_score_calc(self):
        self.right_score +=1
        self.update_score() 
    def l_score_calc(self):
         self.left_score +=1
         self.update_score()
scoreboard=Scoreboard()

while game_on:
    screen.update()
    ball.move()
    if ball.ycor()>240 or ball.ycor()<-250:
          ball.bounce_wall()
    if ball.distance(paddle_right)<50 and ball.xcor()>320:
         ball.bouce_paddel()
    if ball.distance(paddle_left)<50 and ball.xcor()<-320:
         ball.bouce_paddel()
    if ball.xcor()>340 or ball.xcor()<-340:
        time.sleep(1)
        
        if ball.xcor()>340:
            scoreboard.l_score_calc()
            ball.ball_refresh()
        if ball.xcor()<-340:
            scoreboard.r_score_calc()
            ball.ball_refresh()

screen.exitonclick()
