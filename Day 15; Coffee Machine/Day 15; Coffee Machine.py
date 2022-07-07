# Day 15: Coffee Machine

from Coffee_Data import MENU, resources

device = "on"
resources["money"] = 0
successful_transaction = True

while device == "on":

    # Prompt user by asking 'What would you like? (espresso/latte/cappuccino):'
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    total_money = 0

    # Turn off the Coffee Machine by entering 'off' to the prompt.
    if choice == "off":
        device = "off"

    # Print report.
    def report(amount_resources):
        if choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")

    # Check if resources are sufficient?
    enough_resources = True
    for coffee_choice in MENU:
        if coffee_choice == choice:
            for resource in MENU[coffee_choice]["ingredients"]:
                if resources[resource] < MENU[coffee_choice]["ingredients"][resource]:
                    print(f"Sorry, there is not enough {resource}")
                    enough_resources = False
                    break

    # Process coins.
    if choice != "report":
        if enough_resources:
            price = MENU[choice]["cost"]
            print(f"You have to pay ${price:.2f}.")
            quarters = float(input("How many quarters: ")) * float(0.25)
            dimes = float(input("How many dimes: ")) * float(0.10)
            nickles = float(input("How many nickles: ")) * float(0.05)
            pennies = float(input("How many pennies: ")) * float(0.01)
            money_given = quarters + dimes + nickles + pennies

    # Check if transaction is successful
            if price == money_given:
                resources["money"] += money_given
            elif price > money_given:
                print("Sorry that's not enough money. Money refunded.")
                successful_transaction = False
            elif price < money_given:
                refund = money_given - price
                resources["money"] -= refund
                resources["money"] += money_given
                print(f"The refund is: {refund:.2f}")

    # Make Coffee.
    def make_coffee():
        for flavour in MENU:
            if flavour == choice:
                for ingredient in MENU[coffee_choice]["ingredients"]:
                    if resources[ingredient] > MENU[flavour]["ingredients"][ingredient]:
                        resources[ingredient] = resources[ingredient] - MENU[flavour]["ingredients"][ingredient]
                if enough_resources:
                    print(f"Here is your {flavour}. Enjoy!")

    report(resources)
    if successful_transaction:
        make_coffee()



