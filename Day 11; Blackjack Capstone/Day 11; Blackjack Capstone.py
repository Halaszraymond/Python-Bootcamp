# Day 11: Blackjack_capstone_project

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ]


def blackjack():
    # Player_cards
    your_card1 = int(cards[random.randint(0, 12)])
    your_card2 = int(cards[random.randint(0, 12)])
    your_cards = [your_card1, your_card2]
    your_score = your_card1 + your_card2
    print(f"Your cards: {your_cards}, current score: {your_score}")
    for card in your_cards:
        if card == 11 and (your_score > 21):
            your_cards[card] = 1

    # Computer_cards
    pc_card1 = int(cards[random.randint(0, 12)])
    print(f"Computer's first card: {pc_card1}")
    pc_card2 = int(cards[random.randint(0, 12)])
    computer_cards = [pc_card1, pc_card2, ]
    computer_score = pc_card1 + pc_card2
    for card in computer_cards:
        if card == 11 and (computer_score > 21):
            computer_cards[card] = 1

    # Determine_if_the_computer_gets_extra_cards
    while computer_score < 17:
        computer_cards.append(int(cards[random.randint(0, 12)]))
        computer_score += computer_cards[-1]

    # Determine_if_someone_has_Blackjack
    if computer_score == 21:
        print(f"Your final hand: {your_cards}, final score: {your_score}")
        print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You lose...")
        return
    elif your_score == 21:
        print(f"Your final hand: {your_cards}, final score: {your_score}")
        print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
        print("Congratulations! You won this round!")
        return

    # Extra_card
    while your_score < 21:
        extra_card = input("Type 'y' to get another card, type 'n' to pass.\n")
        if extra_card == 'y':
            new_card = int(cards[random.randint(0, 12)])
            your_cards.append(new_card)
            your_score = your_score + new_card
            print(f"Your cards: {your_cards}, current score: {your_score}")
            if your_score == 21:
                print(f"Your final hand: {your_cards}, final score: {your_score}")
                print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
                print("Congratulations! You won this round!")
                return
            if your_score > 21:
                print(f"Your final hand: {your_cards}, final score: {your_score}")
                print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You lose...")
                return

        # Determine_the_winner_and_loser
        elif extra_card == 'n':
            if your_score > computer_score:
                print(f"Your final hand: {your_cards}, final score: {your_score}")
                print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
                print("Congratulations! You won this round!")
                return
            elif your_score < computer_score:
                if computer_score > 21:
                    print(f"Your final hand: {your_cards}, final score: {your_score}")
                    print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("Congratulations! You won this round!")
                    return
                else:
                    print(f"Your final hand: {your_cards}, final score: {your_score}")
                    print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You lose...")
                    return
            else:
                print(f"Your final hand: {your_cards}, final score: {your_score}")
                print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
                print("It's a draw!")
                return


# Executing_of_the_code
while input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n") == 'y':
    print(logo)
    blackjack()
else:
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n") == 'n':
        print("Too bad, you can still choose 'y'")
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n") == 'y':
            print(logo)
            blackjack()
# Totaal_bestede_tijd:_4 uur_(1_uur_beeldmateriaal,_3_uur_oefeningen)
