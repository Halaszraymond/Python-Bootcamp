from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
a_random_word = {}
to_learn = {}

# if words_to_learn file doesnt exist
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# picking a random word
def random_word():
    global a_random_word, flip_timer
    window.after_cancel(flip_timer)
    a_random_word = random.choice(to_learn)
    canvas.itemconfig(image, image=front_card_image)
    canvas.itemconfig(upper_text, text="Spaans", fill="black")
    canvas.itemconfig(lower_text, text=a_random_word["Spaans"], fill="black")
    window.after(3000, func=switch_to_nl)


# Remove words that I already know from the dictionary
def known_word():
    to_learn.remove(a_random_word)
    pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_word()


# switch to the dutch side of the card
def switch_to_nl():
    canvas.itemconfig(upper_text, text="Nederlands", fill="white")
    canvas.itemconfig(lower_text, text=a_random_word["Nederlands"], fill="white")
    canvas.itemconfig(image, image=back_card_image)


# creating a window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=switch_to_nl)

# import images
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# front canvas and random word
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=front_card_image)
upper_text = canvas.create_text(400, 150, text="Taal", fill="black", font=("arial", 40, "italic"))
lower_text = canvas.create_text(400, 263, text="Woord", fill="black", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# right button
right_button = Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

# wrong button
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(column=0, row=1)

random_word()

window.mainloop()
