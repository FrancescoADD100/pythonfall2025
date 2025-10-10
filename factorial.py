"""Assignment: Calculating Factorials
Objective: Write a Python program using a recursive function to calculate the factorial of a number. A recursive function is a function that calls itself to solve a problem.

Assignment Instructions:
Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
For the recursive step, return n * factorial(n-1) if n > 1.
Prompt the user for a non-negative integer and call factorial, printing the result."""

def factorial(n):

    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
       
        # Recursive case
        return n * factorial(n - 1)
    
def main():

    # Prompt user for a non-negative integer
    number = int(input("Enter a non-negative integer: "))
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()
    