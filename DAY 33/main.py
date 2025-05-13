import requests
import json
from tkinter import *
from PIL import Image, ImageTk



win = Tk()
win.geometry("600x700")
# win.config(bg="white")
def kayne_quotes():
    response = requests.get("https://api.kanye.rest")
    print(response)
    response.raise_for_status()
    data=response.json()
    quote = data["quote"]
    canvas.itemconfig(kanye_tex,text=quote)

image = Image.open("D:/100 Days Of Python/DAY 33/background.png")
resized_img = image.resize((400, 600))
photo = ImageTk.PhotoImage(resized_img)

canvas = Canvas(win, height=600, width=400, highlightthickness=0, bg="white")
canvas.place(y=20, x=100)
canvas.create_image(200, 300, image=photo)
kanye_tex=canvas.create_text(200,200,text="quote",font=("Arial",30,"bold"),width=380)
kayn_image = PhotoImage(file="D:/100 Days Of Python/DAY 33/kanye.png")
kanye_button = Button(image=kayn_image,highlightthickness=0,command=kayne_quotes)
kanye_button.place(x=420,y=500)


win.mainloop()