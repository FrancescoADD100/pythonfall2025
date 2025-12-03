"""Objective
Your program should ask the user for their birth month and then display the calendar for that month in the current year.

Requirements
Your program must be contained within a main() function.
Use the Python input() function to ask the user for their birth month (as an integer).
Ensure your program can handle invalid inputs gracefully.
Use Python's datetime module to find the current year.
Generate and display the calendar for the user's birth month in the current year.
Format the calendar output so it is easy to read and understand.
 

Steps
Start by importing the necessary modules: calendar and datetime.
Create a main() function where your program's logic will reside.
Inside main(), get the current year using datetime.datetime.now().year.
Ask the user to enter their birth month and store it in a variable.
Validate the user input to ensure it's an integer between 1 and 12.
Use the Calendar module to generate the calendar for the given month and year.
Print the calendar to the console in a readable format.
Don't forget to call the main() function at the end of your script.
 

Tips and Hints
Remember to handle cases where the user input might be invalid. For example, if the user inputs a string or a number outside the 1-12 range, your program should handle these gracefully.
To align dates under the correct day of the week, use the calendar.month() function from the Calendar module.
Keep your code organized and comments to make it easy to understand.
Test your program with different inputs to ensure it's robust and handles all scenarios."""

import calendar
from datetime import datetime

def main():
    # Get current year
    current_year = datetime.now().year

    # Ask user for birth month
    while True:
        try:
            month = int(input("Enter your birth month 1-12: "))
            if 1 <= month <= 12:
                break
            else:
                print("Birth month must be numbers 1-12.")
        except ValueError:
            print("Not a number. Please enter your birth month number 1-12.")

    # Display calendar for given month and year
    print("Calendar for your birth month:")
    print(calendar.month(current_year, month))

main()