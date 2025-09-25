"""
In this exercise, you will practice using logical operators (and, or, not) in Python. 
Your task is to create a program that prompts the user for two integer inputs 
and then demonstrate the use of these operators.
User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers. 
Include two examples for each of the following operators: and, or, not 
Display Results: Print the logical statement and its result for each comparison.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input.

"""

# Define variables in their square feet average 
HOUSE = 2200 
CAR = 115 
PHONE = 0.125 

# Prompt user for two integers
first_Sqft = int(input("Enter the first square footage: "))
second_Sqft = int(input("Enter the second square footage: "))

# AND operator examples
print(f"{first_Sqft} > CAR and {second_Sqft} > PHONE: "
      f"{first_Sqft > CAR and second_Sqft > PHONE}")

print(f"{first_Sqft} < HOUSE and {second_Sqft} < CAR: "
      f"{first_Sqft < HOUSE and second_Sqft < CAR}")

# OR operator examples
print(f"{first_Sqft} == HOUSE or {second_Sqft} == CAR: "
      f"{first_Sqft == HOUSE or second_Sqft == CAR}")

print(f"{first_Sqft} > PHONE or {second_Sqft} < CAR: "
      f"{first_Sqft > PHONE or second_Sqft < CAR}")

# NOT operator examples
print(f"not ({first_Sqft} < CAR): {not (first_Sqft < CAR)}")
print(f"not ({second_Sqft} > HOUSE): {not (second_Sqft > HOUSE)}")