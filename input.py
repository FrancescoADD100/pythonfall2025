"""
    Create a Python application that allows users to input their total budget and the amounts
    spent in various categories. The program will then calculate and display the percentage 
    of the total budget each category represents.
"""

# Get the values from the user for each category
Monthly_income = input("Enter your total monthly income: ")
Housing = input("Enter your budget for Housing: ")
Utilities = input("Enter your budget for Utilities: ")
Groceries = input("Enter your budget for Groceries: ")
Transportation = input("Enter your budget for Transportation: ")
Health_Care = input("Enter your budget for Health Care: ")
Personal_Care = input("Enter your budget for Personal Care: ")
Clothing = input("Enter your budget for Clothing: ")
Debt = input("Enter your budget for Debt: ")

# Calculate the total budget
total_budget = Housing + Utilities + Groceries + Transportation + Health_Care + Personal_Care + Clothing + Debt

# Calculate money left
Money_left = Monthly_income - total_budget

print(f"The total budget spent is {total_budget:.2f}")
print(f"Housing:")