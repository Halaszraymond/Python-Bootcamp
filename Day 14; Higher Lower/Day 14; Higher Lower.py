# Day 14: Higher Lower Game

# importeren van bestanden
from art import logo
from art import vs
from game_data import data
import random

# welkom
print(logo)
print("Welcome to the higher lower game!")

# variabelen
answer = ""
choice = ""
score = 0

# willekeurige item uit lijst
item_a = random.choice(data)
item_b = random.choice(data)

# Totdat het verkeerde antwoord wordt gegeven blijft het spel zich herhalen
while choice == answer:

    # informatie wordt gegeven aan speler
    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}.")
    print(vs)
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}.")

    # Aan de speler wordt een keuze gevraagd
    choice = input("Who has more followers? 'A' or 'B': \n").lower()

    # Het goede antwoord wordt bepaald
    if item_a['follower_count'] >= item_b['follower_count']:
        answer = "a"
    elif item_a['follower_count'] <= item_b['follower_count']:
        answer = "b"

    # punt als het goede antwoord wordt gegeven
    if choice == answer:
        score += 1
        print(f"You're right! Current score: {score}.")

    # Er wordt doorgespeeld met positie b
    item_a = item_b
    item_b = random.choice(data)

# display als er een fout antwoord wordt gegeven
print(f"Sorry, that's wrong. Final score: {score}")

# Totaal bestede tijd: 2 uur (1 uur beeldmateriaal, 1 uur oefeningen)
