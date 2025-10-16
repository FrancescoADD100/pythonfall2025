"""Objective: Write a Python program that includes two functions - one to calculate the area of a square and another for the area of a circle.
Instructions:
Start with Function Definitions:
Define two functions: square and circle.
Each function should take one parameter (side for square, radius for circle).
Write the square Function:
Calculate the area as side * side and display the result: "The area of the square is [result] square units."
Write the circle Function:
Calculate the area using the formula: area = π * radius * radius. Use 3.14 for π.
Display the result: "The area of the circle is [result] square units."
Test Your Functions:
Call square and circle with sample values."""

# Global constant for Pi
PI = 3.14

# Function to calculate area of square
def square(side):

    # Formula for area of square
    area = side * side
    print(f"The area of the square is {area} square units.")

# Function to calculate area of circle
def circle(radius):

    # Formula for area of circle
    area = PI * radius * radius
    print(f"The area of the circle is {area} square units.")

# Functions with sample values
square(4)  
circle(3)  
