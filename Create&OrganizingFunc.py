"""Assignment: Calculating Factorials
Objective: Write a Python program using a recursive function to calculate the factorial of a number. A recursive function is a function that calls itself to solve a problem.

Assignment Instructions:
Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
For the recursive step, return n * factorial(n-1) if n > 1.
Prompt the user for a non-negative integer and call factorial, printing the result."""

def factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial(n-1) if n > 1

# Example usage
def factorial():
    n = int(input("Enter non negative number:"))
    total_amount = factorial(n)
    print(f"factorial of a number is {n}: {total_amount:,.2f}")

factorial()