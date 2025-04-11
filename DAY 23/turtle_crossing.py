import time 
from turtle import Turtle
from turtle import Screen
import random


COLORS  =[
    "#000000",
    "#FF0000",
    "#00FF00",
    "#0000FF",
    "#00FFFF",
    "#FF00FF",
    "#C0C0C0",
    "#808080",
    "#800000",
    "#808000",
    "#008000",
    "#800080",
    "#008080",
    "#000080",
    "#A52A2A",
    "#FF7F50",
    "#FA8072",
    "#D2691E",
    "#FF6347",
    "#DA70D6",
    "#4B0082",
    "#708090",
    "#A9A9A9",
    "#DC143C",
    "#B22222",
    "#32CD32",
    "#2E8B57",
    "#0000CD",
    "#00BFFF"
]


screen = Screen()
screen.setup(width=600,height=600)
screen.listen()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        self.goto(0,-280)
    def goto_start(self):
        self.goto(0,-280)

    def move(self):
        new_y=self.ycor()+10
        self.goto(self.xcor(),new_y)
    def game_over(self):
         self.goto(0,0)
         self.write("GAME OVER",font="Courier")
    def game_level2(self):
        self.goto(0,0)
        self.goto_start()
    def game_win(self):
        self.goto(0,0)
        self.write("YOU WON",align="center",font="Ariel")
class Level(Turtle):
    def __init__(self):
         super().__init__()
         self.penup()
         self.hideturtle()
         self.level_no=1
    def level_board(self):
        self.clear() 
        self.goto(-200,250)
        self.write(f"LEVEL={self.level_no}",align="center",font="Ariel")
    def level_counter(self):
         self.level_no +=1
         self.level_board()

class Car():
    def __init__(self):
        super().__init__()
        self.all_car=[]
    def create_car(self):
            choice = random.randint(1,6)
            if choice== 1:
                new_car=Turtle()
                new_car.shape("square")
                new_car.shapesize(stretch_len=2 ,stretch_wid=1)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                random_y = random.randint(-250,250)
                new_car.goto(330,random_y)
                self.all_car.append(new_car)
    def move_car(self):
        for car in self.all_car:
             car.backward(10)
    def game_level2(self):
        for car in self.all_car:
             car.backward(20)

 
car=Car()
player = Player()
level=Level()
screen.tracer(0)
screen.onkey(player.move,"Up")
game_on = True
current_level=1
level.level_board()
while game_on:
    
    time.sleep(0.1)
    screen.update()
    car.create_car() 
    car.move_car( )
    #collision with car of turtle
    for cars in car.all_car:
         if cars.distance(player)<20:
            player.game_over()
            game_on=False
    if player.ycor()>280 and current_level==1:
        car.game_level2()
        player.game_level2()
        current_level =2
        level.level_counter()

    if player.ycor()>280 and current_level==2 :
            player.game_win()
            game_on=False
        

screen.exitonclick()

