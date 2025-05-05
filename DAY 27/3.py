import tkinter as tk

win = tk.Tk()
win.minsize(height=500,width=500)
win.config(padx=20,pady=20)
label = tk.Label(text="This is a grid Label",font=("Times New Roman",10))
# label.pack()
label.grid(column=0,row=0)
button = tk.Button(text="click", font=("Times New Roman",15))
# button.pack()
button.grid(column=2,row=0)

button2 = tk.Button(text="click", font=("Times New Roman",15))
# button.pack()
button2.grid(column=1,row=1)

entry = tk.Entry()
entry.grid(column=3,row=2)
win.mainloop()
