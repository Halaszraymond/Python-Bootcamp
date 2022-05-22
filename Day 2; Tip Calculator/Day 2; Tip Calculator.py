# Day 2: Tip_calculator

print("Welcome to the tip calculator.")  # Welkomst schermpje
Bill = input("What was the total of the bill? $\n")  # Gebruiker voert het totaal van de bedrag in
# Gebruiker voert de gewenste fooi percentage in
Tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15?\n")
Total_amount = ((float(Tip_percentage)/100) * float(Bill)) + float(Bill)  # Het totale te betalen bedrag inclusief fooi
people = input("How many people to split the bill?\n")  # Gebruiker voert aantal personen in
Amount_per_person = "{:.2f}".format(float(Total_amount / int(people)))  # Het totale te betalen bedrag per persoon
print(f"Each person should pay: ${Amount_per_person}")  # Display met het te betalen bedrag per persoon

# Totaal aantal uur besteed: 2 uur (1.20 uur beeldmateriaal, +- 40 minuten oefeningen)
