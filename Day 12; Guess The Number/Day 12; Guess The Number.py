# Day 12: Guess The Number

# welcome
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a nubber between 1 and 100.")

# level choice
level_choice = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
if level_choice == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")

# choosing a random number
random_number = random.randint(0, 100)

# process user's choice
guess_number = int(input("Make a guess: "))

# using while loop to determine if the number is guessed
while guess_number != random_number:
    if attempts == 1:
        print("You've run out of guesses, you lose")
        break
    else:
        if guess_number > random_number:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))
        elif guess_number < random_number:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))
if guess_number == random_number:
    print(f"You got it! The answer was {random_number}.")

# Totaal bestede tijd: 2.5 uur (1 uur beeldmateriaal, 1,30 uur oefeningen
