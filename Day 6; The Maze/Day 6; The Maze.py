# Day 6: Maze game

# Het maken van een eigen functie
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Uitvoeren van een taak totdat er is voldaan aan een conditie


while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
        else:
            turn_right()
    elif front_is_clear():
        move()
    else:
        turn_left()


# Kopieer en plak de code in:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en
# .json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json ,voor de uitvoering van de code


