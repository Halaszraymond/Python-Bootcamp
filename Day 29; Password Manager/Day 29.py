from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas for the image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:", font=("arial", 9))
website_label.grid(column=0, row=1)

# Website Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Label
username_label = Label(text="Email/Username:", font=("arial", 9))
username_label.grid(column=0, row=2)

# Email/Username Entry
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "dummy@yahoo.com")

# Password Label
password_label = Label(text="Password:", font=("arial", 9))
password_label.grid(column=0, row=3)

# Password Entry
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Generate Password Button
generate_button = Button(text="Generate Password", width=14, font=("arial", 9), command=password_generator)
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, font=("arial", 9), command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
