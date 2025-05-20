from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface(Tk):
    def __init__(self, quiz_brain):
        super().__init__()
        self.title("Trivia Quiz")
        self.config(padx=20,pady=20, bg=THEME_COLOR)
        self.score_label =Label(text="Score:0",fg="white",bg =THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text =self.canvas.create_text(150,125,text="Some text",fill=THEME_COLOR,font=("Ariel",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.true_image = PhotoImage(file="D:/100 Days Of Python/DAY 34/quizzler-app-start/images/true.png")
        self.true_button =Button(image=self.true_image,highlightthickness=0)
        self.true_button.grid(row=2,column=0)
        self.false_image = PhotoImage(file="D:/100 Days Of Python/DAY 34/quizzler-app-start/images/false.png")
        self.false_button =Button(image=self.false_image,highlightthickness=0)
        self.false_button.grid(row=2,column=1)
        self.mainloop()
        

