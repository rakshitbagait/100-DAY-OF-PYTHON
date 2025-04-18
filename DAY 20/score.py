from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,250)
        self.score= 0
        
        self.color("white")
        self.write(f"Score{self.score}",align="center",font=("Arial",24, "normal" ))
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score{self.score}",align="center",font=("Arial",24, "normal" ))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("Game over",align="center", font="Arial")