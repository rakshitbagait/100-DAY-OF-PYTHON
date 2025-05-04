import tkinter

window = tkinter.Tk()

window.title("MY first gui")
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="this is my label",fg="red",bg="yellow",height=20,width=20)
my_label.pack()

my_label["text"]="new text"
# my_label.config(text="new text")
def button_clicked():
    print("I got clicked")
    my_label.config(text="button is clicked")
button = tkinter.Button(text="this is a button",height=20,width=40,highlightbackground="grey",cursor="arrow",command=button_clicked)
button.pack(side="top")

# entry

input =tkinter.Entry().pack()

window.mainloop() 