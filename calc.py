"""Objective:
Write a Python function named calculate_interest that computes and returns simple interest based on given parameters. (Note - you will call the function from the main() function, main is required!
Background
Simple interest is calculated using the formula:
Simple Interest = (Principal Amount × Rate of Interest × Time) / 100
Function Requirements
A main function should control the logic of the program
Create and call a function should be named calculate_interest.
It should take three parameters that you get from the user:
principal - The initial amount.
rate - The annual interest rate (percentage).
time - The investment duration in years.
Use the return keyword to send back the computed interest to a variable in the main function.
Print the result using formatted strings in the main function.
Example
If you call calculate_interest(1000, 5, 2), the function should return 100 as the simple interest.
Task Instructions
Define the function calculate_interest with appropriate parameters.
In main request the three parameters from the user, then pass them as variable.
Apply the formula to calculate the simple interest.
Return the calculated interest.
Print the result using an f-string:
print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
Sample Output:"""

def calculate_interest(principal, rate, time):

    # Calculate simple interest with formula
    interest = (principal * rate * time) / 100
    return interest

def main():

    # Ask user for three values
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (percentage): "))
    time = float(input("Enter time in years: "))

    # Call function
    simple_interest = calculate_interest(principal, rate, time)

    # Print result
    print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${simple_interest:,.2f}.")

main()

