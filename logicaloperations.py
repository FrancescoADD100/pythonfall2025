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
House = 2200 
Car = 115 
Phone = 0.125 

# Prompt user for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# and operator examples
if num1 > Car and num2 > Phone:
    print(f"{num1} > Car and {num2} > Phone: {num1 > Car and num2 > Phone}")
else:
    print(f"{num1} > Car and {num2} > Phone: {num1 > Car and num2 > Phone}")

if num1 < House and num2 < Car:
    print(f"{num1} < House and {num2} < Car: {num1 < House and num2 < Car}")
else:
    print(f"{num1} < House and {num2} < Car: {num1 < House and num2 < Car}")

# or operator examples
if num1 == House or num2 == Car:
    print(f"{num1} == House or {num2} == Car: {num1 == House or num2 == Car}")
else:
    print(f"{num1} == House or {num2} == Car: {num1 == House or num2 == Car}")

if num1 > Phone or num2 < Car:
    print(f"{num1} > Phone or {num2} < Car: {num1 > Phone or num2 < Car}")
else:
    print(f"{num1} > Phone or {num2} < Car: {num1 > Phone or num2 < Car}")

# not operator examples
if not num1 < Car:
    print(f"not ({num1} < Car): {not (num1 < Car)}")
else:
    print(f"{num1} < Car: {num1 < Car}")

if not num2 > House:
    print(f"not ({num2} > House): {not (num2 > House)}")
else:
    print(f"{num2} > House: {num2 > House}")