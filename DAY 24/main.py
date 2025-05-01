from turtle import Screen
from snake import Snake
import time
from food import Food
from score import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.cv._rootwindow.resizable(False, False)
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect collision with food
    if snake.head.distance(food)<15 :
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        scoreboard.reset()
        snake.reset()
        # game_is_on=False
    # detect collision with tail
    # if the head colides with any segment in the tail
    
    for segment in snake.segments:
        if segment==snake.head:
            pass

        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            # game_is_on=False
            # scoreboard.game_over()

screen.exitonclick()                    