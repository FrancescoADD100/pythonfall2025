""" this assignment, you will create a program that asks the user for their birthday and then calculates their age in different units such as years, months, days, hours, and minutes. This exercise will help you practice using the datetime and timedelta modules in Python.

Assignment Objectives:
Ask the user to input their birthday.
Calculate the user's age in years, months, days, hours, and minutes.
Provide detailed comments to all of the code, explaining what each line that has to do with time calculation does.
Display the results in a user-friendly format.
Implement the solution inside a main() function.
Instructions:
Create a Python script that performs the following steps:

Define a main() function where your program logic will reside.
Use my start program from GitHub: startprogramLinks to an external site.
You can view the classroom demonstration of how we got to the code at the top of the page.
Comment explaining each line of the code
Finish the code to get and display:
months
weeks
days (done)
years (done)
Format and print the results in a clear, understandable manner.
Tips:
To calculate the age in years, you might need to consider leap years. A simple approach is to divide the total number of days by 365.25.
For months, first calculate the years, then use the remaining days to estimate the months.
For weeks, calculate by dividing days by 7
Use try-except blocks to handle any potential input errors."""

from datetime import datetime

def main():
    
    try:
        # Get today's date
        today = datetime.today()
        
        # Ask the user for their birth year, month, and day
        birth_year = int(input("What year were you born?  "))
        birth_month = int(input("What month were you born? (1-12)  "))
        birth_day = int(input("What day of the month were you born?  "))
        
        # Create a datetime object for user's birthday
        birthday = datetime(birth_year, birth_month, birth_day)
        
        # Display user's birthday 
        print("Your birthday is: ")
        print(birthday.strftime("%Y-%m-%d"))
        
        # Calculate difference between today and birthday
        delta = today - birthday
        
        # Age in days
        days = delta.days
        
        # Age in years 
        years = days // 365.2425  
        
        # Remaining days after full years
        remaining_days = days % 365.2425
        
        # Approximate months from remaining days
        months = remaining_days // 30.41
        
        # Age in weeks
        weeks = days // 7
        
        # Display results 
        print("\nYour age is approximately:")
        print(f"{int(years)} years")
        print(f"{int(months)} months")
        print(f"{int(weeks)} weeks")
        print(f"{days} days")
        
    # Handle errors
    except Exception as e:
            print(f"Oops! Something went wrong: {e}")

main()