"""
    Accept a numeric grade from the user and display the letter grade.
    The grading scale is 90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F.
"""

# Define a function to calculate letter grade based on numerical grade
# Get the users grade
numerical_grade = int(input("What numerical grade did the user get?"))

# Check what numerical grade you need to be outside of the 100-0 grading range
if numerical_grade > 100 or numerical_grade < 0: letter_grade = ("Error")

# Check what numerical grade you need for a A
elif numerical_grade >= 90: letter_grade = ("A")

# Check what numerical grade you need for a B
elif numerical_grade >= 80: letter_grade = ("B")

# Check what numerical grade you need for a C
elif numerical_grade >= 70: letter_grade = ("C")

# Check what numerical grade you need for a D
elif numerical_grade >= 60: letter_grade = ("D")

# Check what numerical grade you need for F
else: letter_grade = ("F")

print("The letter grade is:", str(letter_grade))