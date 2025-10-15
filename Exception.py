"""Enhance a basic Python program by implementing try and except statements to handle errors in user input, focusing on data type errors.

Starting Code

# Simple Python program to calculate the square of a number

def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}.")

square_number()
    
Instructions
Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle incorrect data types with an error message.
Test Your Code: Ensure the exception handling works correctly with various inputs.
GitHub Upload: Upload your py file to GitHub and hand in the link
 """

def square_number():
    # Ask user to enter a number and calculate its square
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Call function
square_number()

