"""Objective: Use a generator function with the yield statement in Python to generate all possible two-letter combinations from a given set of characters.

Background:
Generators in Python are a powerful tool for creating iterators in a memory-efficient way. The yield statement is used to produce a sequence of values over time, pausing the function execution between each one.

Task:
Create a Python program that uses a generator function to produce all possible two-letter combinations from a given list of characters. For example, if the list is ['a', 'b', 'c'], the program should generate 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'.

Instructions:
Define a generator function two_letter_combinations that takes a list of characters as an argument.
Use nested loops within the generator function to iterate over the list of characters. In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination.
In the main method, call the generator function with a list of characters and iterate over the generator to print each combination. Create an original  5-letter list.
Include comments in your code to explain the logic behind the generator function and the use of the yield statement.
 

Example:

def two_letter_combinations(characters):
    # Implement the generator function

def main():
    # Call the generator function and print each combination


main()

"""

def two_letter_combinations(characters):

    # Possible two letter combinations
    for char1 in characters:
        for char2 in characters:
            # Yield the combination 
            yield char1 + char2

def main():
    # List of characters 
    characters = ['a', 'b', 'c', 'd', 'e']
    
    # Print combination
    for combination in two_letter_combinations(characters):
        print(combination)

main()