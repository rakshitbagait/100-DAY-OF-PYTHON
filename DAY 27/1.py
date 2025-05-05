import tkinter

window = tkinter.Tk()

window.title("MY first gui")
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="this is my label",fg="red",bg="yellow",height=20,width=20)
my_label.pack()

my_label["text"]="new text"
input =tkinter.Entry()
input.pack()
# my_label.config(text="new text")
def button_clicked():
    print("I got clicked")
    new_text =input.get()
    my_label.config(text=new_text)
    
    
button = tkinter.Button(text="this is a button",height=20,width=40,highlightbackground="grey",cursor="arrow",command=button_clicked)
button.pack(side="top")

# entry
def IntVar():
    print("rakshit")
radio_state = IntVar()
radio = tkinter.Radiobutton(text="opetion",relief="ridge",variable=radio_state,value=1)
radio.pack()

window.mainloop() 