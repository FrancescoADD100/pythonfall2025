"""
Write a Python program that uses if-else statements and: Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.
Remember: Comment your code to explain the functionality of each section.
Handle edge cases, such as ages, precisely at the thresholds.
"""
# Ask the user for their age and convert the input to an integer
age = int(input("How old are you?: "))

# Check if the user is old enough to drive
if age < 16:
    print("You are not old enough to drive.")
if age >= 16:
    print("You are old enough to drive.")
    
# Check if the user can vote
if age >= 18:
    print("You are old enough to vote.")
if age < 18:
    print("You are not old enough to vote.")

# Check if the user can legally buy alcohol
if age >= 21:
    print("You are old enough to legally buy alcohol.")
if age < 21:
    print("You are not old enough to legally buy alcohol.")
# Check if the user is eligible for a senior discount
if age < 65:
    print("You are not eligible for a senior discount.")
elif age >= 65:
    print("You are eligible for a senior discount.")

