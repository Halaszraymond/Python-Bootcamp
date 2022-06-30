from flask import Flask
import random

app = Flask(__name__)

random_number = str(random.randint(0, 9))
too_high = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
too_low = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
right_answer = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"


@app.route('/')
def home_screen():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='http://www.reddit.com/r/perfectloops/comments/1gcxq0/the_numbers_game_oc/'>"


@app.route('/<number>')
def guess_number(number):
    if number == random_number:
        return "<h1 style='background-color:Green;'>You found me!</h1>" \
               f"<img src='{right_answer}'>"
    elif number > random_number:
        return "<h1 style='background-color:Purple;'>Too high, try again!</h1>" \
               f"<img src='{too_high}'>"
    else:
        return "<h1 style='background-color:Red;'>Too low, try again!</h1>" \
               f"<img src='{too_low}'>"
