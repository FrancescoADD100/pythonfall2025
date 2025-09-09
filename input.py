"""
    Create a Python application that allows users to input their total budget and the amounts
    spent in various categories. The program will then calculate and display the percentage 
    of the total budget each category represents.
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
print(f"Transportation: {(Transportation / Monthly_income)}")
print(f"Health_Care: {(Health_Care / Monthly_income):.2%}")
print(f"Personal_Care: {(Personal_Care / Monthly_income):.2%}")
print(f"Clothing: {(Clothing / Monthly_income):.2%}")
print(f"Debt: {(Debt / Monthly_income):.2%}")