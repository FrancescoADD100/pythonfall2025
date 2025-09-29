"""
Objective:
Create a Python script to track heart rate readings and calculate the average heart rate.
Requirements:
1. Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
2. Use a loop to prompt the user for heart rate (in BPM) at each time slot.
3. Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
4. Print each individual reading in a sentence.
5. Calculate the average heart rate and display it.
Sample Output:
At Morning my heart rate was 70 BPM
At Midday my heart rate was 75 BPM
At Afternoon my heart rate was 72 BPM
At Evening my heart rate was 68 BPM
Your average heart rate for the day is: 71.25 BPM
"""

# Define time slots
time_of_day = ["Morning", "Midday", "Afternoon", "Evening"]

# Heart rates list
heart_rates = []
for time in time_of_day:
    bpm = int(input(f"Enter your heart rate (BPM) for {time}: "))
    heart_rates.append([time, bpm])

# Display individual readings
for time, bpm in heart_rates:
    print(f"At {time} my heart rate was {bpm} BPM")
    
# Calculate average heart rate
average_bpm = sum(bpm for _, bpm in heart_rates) / len(heart_rates)
print(f"Your average heart rate for the day is: {average_bpm:.2f} BPM")