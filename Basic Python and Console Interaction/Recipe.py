"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""

# Write program here...


_green = input("Enter ingredient 1: ")
_gOunces = float(input("Ounces of mixed greens: " + _green))

_blue = input("Enter ingredient 2: ")
_bOunces = float(input("Ounces of blueberries: "+ _blue))

_walnuts = input("Enter ingredient 3: ")
_wOunces = float(input("Ounces of walnuts: "+_walnuts))

_servings = int(input("Number of servings: "))

print("Total ounces of " + _green + ": "+str(_gOunces*_servings))
print("Total ounces of "+ _blue + ": "+str(_bOunces*_servings))
print("Total ounces of "+_walnuts +": "+str(_wOunces*_servings))