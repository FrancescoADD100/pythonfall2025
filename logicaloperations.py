"""
In this exercise, you will practice using logical operators (and, or, not) in Python. 
Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.
"""

# Define variables
House = ("2200 sqft")
Car = ("115 sqft")
Phone = ("0.125 sqft")

# and operator 
if House > Car and House > Phone: print("House is the biggest")

elif Car < House and Car > Phone: print("Car is the biggest")

else: print("Phone is the biggest")

# or operator
if House > Car or House > Phone: print("House is the biggest")

elif Car < House or Car > Phone:  print("Car is the biggest")

else: print("Phone is the biggest")

# not operator
if not House > Car: print("House is not bigger than Car")

else: print("House is bigger than Car")
