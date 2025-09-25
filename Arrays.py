"""
In this assignment, you will create a Python program to track your daily heart rate at different times and calculate the average.
Objective:Create a Python script to track heart rate readings and calculate the average heart rate.
Requirements: Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it.
"""

# Define time slots
time_of_day = ["Morning", "Midday", "Afternoon", "Evening"]

# Heart rates list
heart_rates = []
for time in time_of_day:
    bpm = int(input(f"Enter your heart rate (BPM) for {time}: "))
    heart_rates.append([time, bpm])


# Calculate average heart rate
average_bpm = sum(bpm for _, bpm in heart_rates) / len(heart_rates)
print(f"Your average heart rate for the day is: {average_bpm:.2f} BPM")