from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if (website_entry.get() == "" or password_entry.get() == "" or website_entry.get().isspace()
            or password_entry.get().isspace()):
        messagebox.showinfo(title="Error", message="Don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_entries:
                # Reading old data
                data = json.load(data_entries)
        except FileNotFoundError:
            with open("data.json", "w") as data_entries:
                json.dump(new_data, data_entries, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_entries:
                # Saving updated data
                json.dump(data, data_entries, indent=4)
        finally:
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)
            email_username_entry.insert(0, "@gmail.com")


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data_entries:
            data = json.load(data_entries)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"E-mail: {data[website]["email"]}\n"
                                                       f"Password: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(56, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="W")
website_entry.focus()

search_button = Button(text="Search", width="11", command=find_password)
search_button.grid(column=1, row=1, sticky="E")

email_username_label = Label(text="Email/Username")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, sticky="EW")
email_username_entry.insert(0, "@gmail.com")

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=17, show="*")
password_entry.grid(column=1, row=3, sticky="W")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=1, row=3, sticky="E")

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, sticky="EW")

window.mainloop()
