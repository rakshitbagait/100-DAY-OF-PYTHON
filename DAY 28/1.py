WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0

from tkinter import *
from PIL import Image, ImageTk
import math
win = Tk()
win.geometry("400x600")
win.title("POMODORO")
win.config(padx=0,pady=50,background="yellow")
win.resizable(False,False)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
     win.after(1000,count_down,count-1)
def start_timer():
   global reps 
   reps +=1
   work_sec = WORK_MIN*60
   short_break_sec = SHORT_BREAK_MIN*60
   long_break_sec= LONG_BREAK_MIN*60
   if reps%8==0:
     count_down(long_break_sec)
   elif reps%2==0:
    count_down(short_break_sec)
   else:
         count_down(work_sec)
    

timer_label = Label(text="Timer",foreground="Green",font=("Times New Roman",60,"bold"),background=win["background"])
timer_label.pack() 

# start_button.pack()
canvas = Canvas(width=520, height=520,background="yellow",highlightthickness=0)
canvas.pack()

# Load image using PIL
img = Image.open("D:/100 Days Of Python/DAY 28/image.png")
photo = ImageTk.PhotoImage(img)

canvas.image = photo  # Keep reference
canvas.create_image(200, 200, image=photo)
timer_text = canvas.create_text(200,200,text="00:00",font=("Times New Roman",40,"bold"),fill="white")
canvas.pack(anchor="center",)

start_button = Button(text="start",font=("times new roman",10),fg="white",bg="green",height=2,width=5,command=start_timer)
start_button.place(x=50,y=500)
reset_button = Button(text="reset",font=("times new roman",10),fg="white",bg="green",height=2,width=5)
reset_button.place(x=300,y=500)

win.mainloop()
