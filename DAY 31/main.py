from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("D:/100 Days Of Python\DAY 31\data/french_words.csv")

to_learn =data.to_dict(orient="records")
print(to_learn)
win = Tk()
# win.geometry("800x500")
# win.resizable(False, False)
global current_card
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_img,image=card_front_img)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    flash_timer=win.after(3000,func=flip_card)
    
    
def flip_card():
    canvas.itemconfig(card_img,image=card_back_img)
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])

def is_know():
    to_learn.remove(current_card)
    data= pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn")
    next_card()

    
win.config(background=BACKGROUND_COLOR,padx=50,pady=50)
win.title("Flashy")
right_image=PhotoImage(file="D:/100 Days Of Python/DAY 31/images/right.png")
wrong_image=PhotoImage(file="D:/100 Days Of Python/DAY 31/images/wrong.png")
right_button =Button(image=right_image,highlightthickness=0,command=is_know)
right_button.grid(row=1,column=1)
wrong_button =Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)
card_front_img = PhotoImage(file="D:/100 Days Of Python/DAY 31/images/card_front.png")
card_back_img  = PhotoImage(file="D:/100 Days Of Python/DAY 31/images/card_back.png")

canvas=Canvas(width=800,height=526,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,background=BACKGROUND_COLOR)
card_img=canvas.create_image(400,263,image=card_front_img)
card_title =canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word =canvas.create_text(400,263,text="word",font=("Arial",70,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

next_card()
win.mainloop()