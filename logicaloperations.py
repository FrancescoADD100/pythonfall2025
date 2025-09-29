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
first_sqft = int(input("Enter the first square footage: "))
second_sqft = int(input("Enter the second square footage: "))

# AND operator examples
print(f"{first_sqft} > CAR and {second_sqft} > PHONE: "
      f"{first_sqft > CAR and second_sqft > PHONE}")

print(f"{first_sqft} < HOUSE and {second_sqft} < CAR: "
      f"{first_sqft < HOUSE and second_sqft < CAR}")

# OR operator examples
print(f"{first_sqft} == HOUSE or {second_sqft} == CAR: "
      f"{first_sqft == HOUSE or second_sqft == CAR}")

print(f"{first_sqft} > PHONE or {second_sqft} < CAR: "
      f"{first_sqft > PHONE or second_sqft < CAR}")

# NOT operator examples
print(f"not ({first_sqft} < CAR): {not (first_sqft < CAR)}")
print(f"not ({second_sqft} > HOUSE): {not (second_sqft > HOUSE)}")