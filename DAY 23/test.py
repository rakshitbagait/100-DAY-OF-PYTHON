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
    def move(self):
        new_y=self.ycor()+10
        self.goto(self.xcor(),new_y)
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_car=[]
    def create_car(self):
            choice = random.randint(1,6)
            if choice== 1:
                
                self.shape("square")
                self.shapesize(stretch_len=2 ,stretch_wid=1)
                self.penup()
                self.color(random.choice(COLORS))
                random_y=random.randint(-250,250)
                new_y=self.ycor(random_y)
                self.goto(330,new_y)
                self.all_car.append(self)
    def move_car(self):
        for car in self.all_car:
             car.backward(10)
    
    
car=Car()
player = Player()
screen.tracer(0)
screen.onkey(player.move,"Up")
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car() 
    car.move_car( )
    #collision with car of turtle
    # if player.ycor==car.:
    #      game_on=False

screen.exitonclick()
