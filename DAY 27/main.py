import tkinter as tk

win = tk.Tk()

win.minsize(height=300,width=300)
win.config(padx=50,pady=50)


miles_entry = tk.Entry()
miles_entry.place(x=50,y=50)
miles_lable = tk.Label(text="Miles",font=("Times New Roman",15))
miles_lable.place(x=150,y=50)
is_equal_to = tk.Label(text="is equal to ")
is_equal_to.place(x=0,y=100)
km_result = tk.Label(text="0",font=("Times new roman",15))
km_result.place(x=90,y=100)
km_lable = tk.Label(text="km",font=("Times New Roman",15))
km_lable.place(x=150,y=100)
def calculate ():
    try:
        miles = float(miles_entry.get())
        km = round(miles*1.609,2)
        km_result.config(text=km)
    except ValueError:
        km_result.config(text="invalid")
calculate_button = tk.Button(text="calculate",width=15,command=calculate,)
calculate_button.place(x=50,y=150)
win.mainloop()