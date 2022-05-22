import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
missed_states = []

Game_is_on = True
correct_guesses = []


def text_turtle(state):
    state_data = data[data.state == state]
    Oscar = turtle.Turtle()
    Oscar.hideturtle()
    Oscar.penup()
    Oscar.goto(int(state_data.x), int(state_data.y))
    Oscar.write(state)
    return


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    for state_name in all_states:
        if state_name == answer_state:
            correct_guesses.append(state_name)
            text_turtle(state_name)

for state in all_states:
    if state not in correct_guesses:
        missed_states.append(state)


df = pandas.DataFrame.from_dict(missed_states)
df.to_csv("Missed_states.csv")





