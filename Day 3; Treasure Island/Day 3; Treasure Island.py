# Day 3: treasure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input("Would you like to go to 'the castle' or 'the island'?\n").lower()
if direction == "the castle":
    print("Game over, you were eaten by the dragons who live there.")
elif direction == "the island":
    travel = input("Would you like to 'swim' or 'wait' for a boat?\n").lower()
    if travel == "swim":
        print("Game over, the piranhas were hungry today and thought you were a nice snack.")
    elif travel == "wait":
        door = input(
            "Which house on the island do you think to contain th treasure? 'the wooden', 'the sandstone' or 'the "
            "glass' house?\n").lower()
        if door == "the wooden":
            print("Game over, this house is full of snakes and scorpions")
        elif door == "the sandstone":
            print("Game over, the house collapsed because of weakness of the sand")
        elif door == "the glass":
            print("Congratulations!! You have found the treasure!:)")
        else:
            print("Oops, I didn't hear you right, choose from 'the wooden', 'the sandstone' or 'the glass' door.")
    else:
        print("Oops, I didn't hear you right, choose from 'swim' or 'wait'.")
else:
    print("Oops, I didn't hear you right, choose from 'the castle' or 'the island'.")

# Totaal aantal uur besteed: 3 uur (1.40 uur beeldmateriaal, 1.20 uur oefeningen)
