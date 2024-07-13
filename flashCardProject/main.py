#100DaysOfCode
#TheAppBrewery

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}
dict_data = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dict_data = original_data.to_dict(orient="records")
else:
    dict_data = data.to_dict(orient="records")


def change_word():
    global word, flip_timer
    system.after_cancel(flip_timer)
    word = random.choice(dict_data)
    canvas.itemconfig(upper_text, text="French", fill="black")
    canvas.itemconfig(lower_text, text=word["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = system.after(3000, func=change_card)


def change_card():
    canvas.itemconfig(upper_text, text="English", fill="white")
    canvas.itemconfig(lower_text, text=word["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)


def remove_words():
    dict_data.remove(word)
    new_data = pandas.DataFrame(dict_data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    change_word()


system = Tk()
system.title("Flashy")
system.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = system.after(3000, func=change_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
upper_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
lower_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=change_word)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, bg=BACKGROUND_COLOR, highlightthickness=0, command=remove_words)
right_button.grid(column=1, row=1)

change_word()

system.mainloop()
