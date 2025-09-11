"""
In this exercise, you will practice using logical operators (and, or, not) in Python. 
Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.
"""

# Define variables
House = ("bigger")
Car = ("big")
Phone = ("small")

# and operator 
if House > Car and House > Phone: print("House is bigger")

elif Car < House and Car > Phone: print("Car is big")

else: print("phone is small")

# or operator
if House > Car or House > Phone: print("House is bigger")

elif Car < House or Car > Phone:  print("Car is big")

else: print("phone is small")

# not operator
if not House > Car: print("House is not bigger")

else: print("House is bigger")
