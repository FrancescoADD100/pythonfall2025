"""
    Accept a numeric grade from the user and display the letter grade.
    The grading scale is 90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F.
"""

# Define a function to calculate letter grade based on numerical grade
# Get the users grade
numerical_grade = int(input("W hat numerical grade did the user get?"))

# Check what numerical grade you need for a A
if numerical_grade > 89: letter_grade = ("A")

# Check what numerical grade you need for a B
elif numerical_grade > 79: letter_grade = ("B")

# Check what numerical grade you need for a C
elif numerical_grade > 69: letter_grade = ("C")

# Check what numerical grade you need for a D
elif numerical_grade > 59: letter_grade = ("D")

# Check what numerical grade you need for a F
else: letter_grade = ("F")

print("The letter_grade will be", str(letter_grade))