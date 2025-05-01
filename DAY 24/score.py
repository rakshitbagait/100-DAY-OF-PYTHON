from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(0,250)
        self.score= 0
        self.high_score =0
        self.color("white")

        try:
            with open("Data.txt", "r") as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Arial",24, "normal" ))

        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score{self.score} High Score: {self.high_score}",align="center",font=("Arial",24, "normal" ))
    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("Data.txt", "w") as file:
                file.write(str(self.high_score))
        self.update_scoreboard()
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over",align="center", font="Arial")