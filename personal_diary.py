"""Personal Diary
Create a program named personal_diary.py.
Ask the user for date, time, and a diary entry.
Append the entry to diary.txt (do not overwrite).
Separate each entry with a blank line for readability.
Run your program at least three times to confirm new entries are saved properly."""

def main():
    # Get user input 
    date = input("Enter the date: ")
    time = input("Enter the time: ")
    entry = input("Enter your diary entry: ")

    # Open diary.txt file 
    with open("diary.txt", "a") as diary_file:
        # Print inputs the file
        diary_file.write(f"Date: {date}\n")
        diary_file.write(f"Time: {time}\n")
        diary_file.write(f"Entry: {entry}\n")
        diary_file.write("\n")  # blank line 

main()

