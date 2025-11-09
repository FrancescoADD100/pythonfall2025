"""
Write a short interactive Python program of your choice that uses try and except to catch and respond to at least two specific exceptions. Your program should:

Include a main() function.
Use try and except to catch specific errors like ValueError or ZeroDivisionError.
Provide helpful messages when errors occur.
Do something meaningful or fun—be creative! You could build a number guessing game, a basic calculator, or even a simple quiz with input validation.
"""

def main():

    # Ask the user to guess a number between 1 and 10
    print("Please guess a number between 1 and 10:")

    try:
        guess = int(input("Enter your guess: "))

        # Check if the guess is within the valid range
        if guess < 1 or guess > 10:
            print("That number is out of range. Please enter a number between 1-10.")

            #if the guess is valid, print the guessed number
        else:
            print(f"You guessed: {guess}")

    # See if the user input is not a number
    except ValueError:
        print("That is not a number. Please enter a number between 1-10.")

    except KeyboardInterrupt: print("\nGame interrupted — goodbye!")

main()
