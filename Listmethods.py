"""Welcome to your Python assignment! This task will help you practice working with lists, user input, and basic calculations. Follow the steps below:
Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps.
"""

# List of days in a week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Empty list to store steps
steps = []

# Collect steps for each day
for day in days:
    daily_steps = int(input(f"Enter the number of steps taken on {day}: "))
    steps.append(daily_steps)

# Display steps for each day
for day, daily_steps in zip(days, steps):
    print(f"On {day} you took {daily_steps} steps.")

# Display total and average steps
print("Total steps taken in the week:", sum(steps))
print("Average steps per day:", sum(steps) / len(steps))
