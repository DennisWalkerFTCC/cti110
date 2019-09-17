# Calculates the total amount of a meal purchased at a restaurant
# 9/10/2019
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Dennis Walker
#

""" Pseudocode """
# Ask user for the meal price and store it in a function
# Ask user for the tip percentage and store it
# Ask user for the tax percentage and store it
# Calculate the tip
# Calculate the tax
# Calculate a total of the meal price, the tip, and the tax.
# Display the grand total, the tip, and the tax
# End program


# Stores information provided by user
meal_price = float(input("Input meal price: "))
tip_percent = float(input("Input the tip percentage (in decimal format): "))
tax_percent = float(input("Input the tax percentage (in decimal format): "))

# Calculates the tip, tax, and grand total
tip_total = float(tip_percent * meal_price)
tax_total = float(tax_percent * meal_price)
grand_total = meal_price + tip_total + tax_total

# Prints the tip, tax, and grand total
print(f"\nYour calculated tip is: {tip_total:.2f}$")
print(f"Your calculated tax is: {tax_total:.2f}$")
print(f"Your calculated grand total is: {grand_total:.2f}$")
