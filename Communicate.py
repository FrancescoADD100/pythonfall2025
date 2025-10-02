"""Objective:
Develop a Python-based Madlib based on a song of your choice. The program should collect at least 8 different pieces of information from the user and incorporate them into the song using named arguments. The goal is to practice using functions, user input, and string manipulation in Python.

Important Note:
Choose any song you like for your madlib, but remember, no Rickrolling! Be creative and respectful in your song choice.

Task:
Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.
Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.
Write the Function:
Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
Collect User Input:
Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
Call the Function:
Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function definition.
"""

# Define the function to create a custom song
def custom_song(name, adjective1, noun1, place, verb, adjective2, noun2, emotion ):
    print("\n")
    print(f"{name}, {name}, {adjective1} {noun1},")
    print(f"How I wonder what you are")
    print(f"Up above the {place} so high")
    print(f"Like a {adjective2} {noun2} in the sky")
    print(f"When you {verb}, I feel so {emotion}")
    print(f"{name}, {name}, {adjective1} {noun1}")

# Collect user input
input_name = input("Enter a name: ")
input_adjective1 = input("Enter an adjective: ")
input_noun1 = input("Enter a noun: ")
input_place = input("Enter a place: ")
input_verb = input("Enter a verb: ")
input_adjective2 = input("Enter another adjective: ")
input_noun2 = input("Enter another noun: ")
input_emotion = input("Enter an emotion: ")

# Call the function with named arguments
custom_song(name = input_name, adjective1 = input_adjective1, noun1 = input_noun1, place = input_place, verb = input_verb, adjective2 = input_adjective2, noun2 = input_noun2, emotion = input_emotion)
