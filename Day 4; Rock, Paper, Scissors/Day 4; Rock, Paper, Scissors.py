# Day 4: Rock, Paper, Scissor

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lijst met mogelijkheden:
RPS = [rock, paper, scissors]

# Hier wordt de keuze van de speler verwerkt:
player = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
if player <= 2:
    print("You chose\n" + RPS[int(player)])
else:
    print("You typed an invalid number, pls try again")

# Hier wordt een willekeurige keuze van de computer bepaald:
computer = random.randint(0, 2)
if player <= 2:
    print("Computer chose\n" + RPS[int(computer)])

# Getal wordt string
player = int(player)
computer = int(computer)

# Hier wordt besloten wie er wint:
if player == 0 and computer == 0:
    print("Draw")
elif player == 0 and computer == 1:
    print("You lose")
elif player == 0 and computer == 2:
    print("You win")

if player == 1 and computer == 0:
    print("You win")
elif player == 1 and computer == 1:
    print("Draw")
elif player == 1 and computer == 2:
    print("You lose")

if player == 2 and computer == 0:
    print("You lose")
elif player == 2 and computer == 1:
    print("You win")
elif player == 2 and computer == 2:
    print("Draw")


