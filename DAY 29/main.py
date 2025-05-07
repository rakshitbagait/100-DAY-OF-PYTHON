from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random, string,pyperclip
import json
win = Tk()
win.geometry("600x600")
win.configure(bg="white")
logo_image = Image.open("D:/100 Days Of Python/DAY 29/image.png")  # Replace with your logo path
resized_logo = logo_image.resize((32, 32))  # Resize the image to an appropriate icon size
logo_photo = ImageTk.PhotoImage(resized_logo)

# Set the window icon
win.iconphoto(True, logo_photo)

placeholder_website = "Enter the website Name/Url"
placeholder_email="Enter your email"
placeholder_pass="Enter your password"

def add_function():
    website = website_name_entry.get()
    email = email_name_entry.get()
    password = pass_name_entry.get()
    if email_name_entry.get()!=placeholder_email and website_name_entry.get()!=placeholder_website and pass_name_entry.get()!=placeholder_pass:
        new_data ={website:
                       {
                           "email":email,
                           "password": password
                       }
                       }
        try:
            with open("my_pass_file.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        # Update and save data
        data.update(new_data)
        with open("my_pass_file.json", "w") as file:
            json.dump(data, file, indent=4)
                
    else:
        messagebox.showerror("Input Error",'None of the field must be  empty')
                        
def generate_pass(length = 12):
    random_pass =""
    for char in range(0,length//3):
        letters = random.choice(string.ascii_letters)
        numbers = random.choice(string.digits)
        symbols = random.choice(string.punctuation)
        random_pass += letters + numbers + symbols
    print(random_pass)
    char_list = list(random_pass)
    random.shuffle(char_list)
    final_pass = "".join(char_list)
    print(final_pass)
    if pass_name_entry.get() == placeholder_pass:
        pass_name_entry.delete(0, END)
        pass_name_entry.config(fg="#2196F3")
        pass_frame_underline.config(bg="#e3a90b")

    # Insert password into entry field
    pass_name_entry.delete(0, END)
    pass_name_entry.insert(0, final_pass)
    pyperclip.copy(final_pass)


def search_pass():
    website = website_name_entry.get()
    try:
        with open("my_pass_file.json", 'r') as file:
            data = json.load(file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo("Credentials Found", f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror("Not Found", f"No credentials stored for '{website}'.")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "Password file not found. Add a password first.")
    except json.JSONDecodeError:
        messagebox.showerror("Corrupted File", "The data file is corrupted.")

def on_focus_in(event, entry, placeholder, underline):
    if entry.get() == placeholder:
        entry.delete(0, END)
        entry.config(fg="#2196F3")
    underline.config(bg="#e3a90b")

def on_focus_out(event, entry, placeholder, underline):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="grey")
    underline.config(bg="#ccc")

# Load image
image = Image.open("D:/100 Days Of Python/DAY 29/image.png")
resized_img = image.resize((200, 200))
photo = ImageTk.PhotoImage(resized_img)

canvas = Canvas(win, height=400, width=400, highlightthickness=0, bg="white")
canvas.place(y=-50, x=100)
canvas.create_image(200, 200, image=photo)

# Title Label
one_pass_label = Label(text="One Pass", font=("Times New Roman", 50, "bold"), fg="#11c5d9", bg="white")
one_pass_label.place(x=170, y=260)

# Entry box with placeholder
website_name_entry = Entry(win, bd=0, font=("Segoe UI", 14), bg="white", fg="grey", insertbackground="#333")
website_name_entry.place(x=20, y=410, height=25, width=300)
website_name_entry.insert(0, placeholder_website)
website_name_entry.bind("<FocusIn>", lambda e: on_focus_in(e, website_name_entry, placeholder_website, website_frame_underline))
website_name_entry.bind("<FocusOut>", lambda e: on_focus_out(e, website_name_entry, placeholder_website, website_frame_underline))
website_frame_underline = Frame(win, height=2, width=300, bg="#ccc")
website_frame_underline.place(x=20, y=435)


# email 
email_name_entry = Entry(win, bd=0, font=("Segoe UI", 14), bg="white", fg="grey", insertbackground="#333")
email_name_entry.place(x=20, y=460, height=25, width=300)
email_name_entry.insert(0, placeholder_email)
email_frame_underline = Frame(win, height=2, width=300, bg="#ccc")
email_frame_underline.place(x=20, y=495)
email_name_entry.bind("<FocusIn>", lambda e: on_focus_in(e, email_name_entry, placeholder_email, email_frame_underline))
email_name_entry.bind("<FocusOut>", lambda e: on_focus_out(e, email_name_entry, placeholder_email, email_frame_underline))

pass_name_entry = Entry(win, bd=0, font=("Segoe UI", 14), bg="white", fg="grey", insertbackground="#333")
pass_name_entry.place(x=20, y=515, height=25, width=300)
pass_name_entry.insert(0, placeholder_pass)
pass_frame_underline = Frame(win, height=2, width=300, bg="#ccc")
pass_frame_underline.place(x=20, y=540)
pass_name_entry.bind("<FocusIn>", lambda e: on_focus_in(e, pass_name_entry, placeholder_pass, pass_frame_underline))
pass_name_entry.bind("<FocusOut>", lambda e: on_focus_out(e, pass_name_entry, placeholder_pass, pass_frame_underline))

add_button = Button(
    win,
    text="Add",
    font=("Segoe UI", 10, "bold"),
    fg="white",
    bg="#11c5d9",               # Mustard yellow
    activebackground="#cc900a", # Darker shade on click
    activeforeground="white",
    bd=0,                       # No border
    relief=FLAT,
    padx=10,
    pady=5,
    width=69,
    command=add_function
)

add_button.place(x=20,y=550)

genrate_pass_button = Button(    win,
    text="Generate pass",
    font=("Segoe UI", 10, "bold"),
    fg="white",
    bg="#11c5d9",               # Mustard yellow
    activebackground="#cc900a", # Darker shade on click
    activeforeground="white",
    bd=0,                       # No border
    relief=FLAT,
    padx=10,
    pady=5,
    width=30,
    command=generate_pass)

genrate_pass_button.place(x=330,y=510)

search_button = Button(    win,
    text="Search",
    font=("Segoe UI", 10, "bold"),
    fg="white",
    bg="#11c5d9",               # Mustard yellow
    activebackground="#cc900a", # Darker shade on click
    activeforeground="white",
    bd=0,                       # No border
    relief=FLAT,
    padx=10,
    pady=5,
    width=30,
    command=search_pass)
search_button.place(x=330,y=410)


win.mainloop()
