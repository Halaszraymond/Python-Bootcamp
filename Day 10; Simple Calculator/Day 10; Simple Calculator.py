# Day 10: Simple Calculator

from art import logo


# Onderstaand zijn de handelingen die de rekenmachine moet kunnen


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# Hier worden de inputs gevraagd


def calculator():
    print(logo)
    number_1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    continuation = True

    while continuation:
        operation_symbol = input("Pick an operation: ")
        number_2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(number_1, number_2)
        # Hier worden de inputs verwerkt
        print(f"{number_1} {operation_symbol} {number_2} = {answer}")
        # Gevraagd wordt of de gebruiker door wilt met het berekende antwoord, bij "n" dan begint de rekenmachine
        # opnieuw
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: \n")
        if choice == "n":
            continuation = False
            calculator()
        else:
            number_1 = answer


calculator()

# Aantal bestede tijd: 2,5 uur (1 uur beeldmateriaal, 1,30 uur oefeningen)
