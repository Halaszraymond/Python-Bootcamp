import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = [state_name for state_name in all_states if state_name not in guessed_states]
        df = pandas.DataFrame.from_dict(missed_states)
        df.to_csv("Missed_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        Oscar = turtle.Turtle()
        Oscar.hideturtle()
        Oscar.penup()
        state_data = data[data.state == answer_state]
        Oscar.goto(int(state_data.x), int(state_data.y))
        Oscar.write(answer_state)
