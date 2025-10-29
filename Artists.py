"""
Objective: Write a Python program that handles exceptions related to list operations. Your program will start with a predefined list of the top ten performing artists of all time and will include functionality to modify this list based on user input.

Starting Program:
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here


main()
    
Tasks:
Modify Artist List: Write a function to replace an artist in the top_artists list. The function should ask the user for an index and a new artist name. Ensure your function catches and handles ValueError for invalid number conversion and IndexError for out-of-range indices.
General Error Handling: Modify your function to catch both ValueError and IndexError using a single except block. Provide a general error message like "An input error occurred."
Hints:
Use input() to get user input for the index and new artist name.
Convert the index input to an integer using int(). This might raise a ValueError if the input is not a valid integer.
When replacing an artist in the list, accessing an invalid index will raise an IndexError.
Use a try...except block to catch and handle these exceptions.
Remember that you can catch multiple exceptions in a single block by using a tuple for general error handling.
Example User Interaction:
Enter the index of the artist to replace: 2
Enter the new artist name: Taylor Swift
Updated list: ['The Beatles', 'Madonna', 'Taylor Swift', 'Elvis Presley', ...]

Note to Students: This assignment is designed to test your understanding of exception handling in Python. Focus on how you can make your program robust against invalid user inputs and how to provide informative error messages. Good luck!
"""
def main():
    top_artists = [
        "The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
        "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

    try:
        index = int(input("Enter the index of the artist to replace (0-9): "))
        new_artist = input("Enter the new artist name: ")
        top_artists[index] = new_artist

    except (ValueError, IndexError):
        print("That is not a number or not a number between 0-9, please enter a number between 0-9.")

    else:
        print("Updated list:", top_artists)


main()