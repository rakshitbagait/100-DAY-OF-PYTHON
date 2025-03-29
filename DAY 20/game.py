import time, turtle as tt

screen= tt.Screen()
screen.tracer(0)
root =screen._root
root.resizable(False,False)
screen.setup(width=600,height=600)
screen.bgcolor("cyan")
screen.title("Snake Game")
starting_position =[(0,0),(-20,0),(-40,0)]
snake =[]
for turtle in range(3):
    tim = tt.Turtle()
    tim.penup()
    tim.shape("square")
    tim.color("red")
    tim.goto(starting_position[turtle])
    snake.append(tim)
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    for tail_num in range(len(snake)-1,0,-1):
        new_x =snake[tail_num-1].xcor()
        new_y =snake[tail_num-1].ycor()
        snake[tail_num].goto(new_x,new_y)
    snake[0].forward(20) 
    

screen.exitonclick()