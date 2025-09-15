"""
Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
Housing (rent or mortgage)
Utilities
Groceries
Transportation
Health Care
Personal Care
Clothing
Debt
Calculate the percentage of the total budget spent in each category.
Tell the user how much the spent total, and how much money they have left. 
Display the results in a user-friendly format using f-strings.
Ensure your code is well-commented to explain the functionality of different sections.
"""

# Get the values from the user for each category
Monthly_income = int(input("Enter your total monthly income: "))
Housing = int(input("Enter your budget for Housing: "))
Utilities = int(input("Enter your budget for Utilities: "))
Groceries = int(input("Enter your budget for Groceries: "))
Transportation = int(input("Enter your budget for Transportation: "))
Health_Care = int(input("Enter your budget for Health Care: "))
Personal_Care = int(input("Enter your budget for Personal Care: "))
Clothing = int(input("Enter your budget for Clothing: "))
Debt = int(input("Enter your budget for Debt: "))

# Calculate the total budget
total_budget = Housing + Utilities + Groceries + Transportation + Health_Care + Personal_Care + Clothing + Debt

# Calculate money left
Money_left = Monthly_income - total_budget

print(f"The total budget spent is {total_budget:.2f}")
print(f"Housing: {(Housing / Monthly_income):.2%}")
print(f"Utilities: {(Utilities / Monthly_income):.2%}")
print(f"Groceries: {(Groceries / Monthly_income):.2%}")
print(f"Transportation: {(Transportation / Monthly_income):.2%}")
print(f"Health_Care: {(Health_Care / Monthly_income):.2%}")
print(f"Personal_Care: {(Personal_Care / Monthly_income):.2%}")
print(f"Clothing: {(Clothing / Monthly_income):.2%}")
print(f"Debt: {(Debt / Monthly_income):.2%}")