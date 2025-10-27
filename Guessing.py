"""In this assignment, you will create a Python program that generates a random number between 1 and 100. Your program should allow the user to guess the number, and provide feedback on how close their guess is to the actual number.

Assignment Objectives:
Use the random module to generate a random number.
Implement a while loop to allow continuous guessing until the correct number is guessed.
Use the abs() function to determine the difference between the guess and the actual number.
Provide feedback based on the proximity of the guess to the actual number:
If the difference is within 5, print "Very Hot".
If the difference is within 15, print "Hot".
If the difference is within 25, print "Cool".
If the difference is more than 25, print "Cold".
Make sure to call the main function!
After completing the program, upload it to your GitHub repository.
Submit the link to your GitHub repository in Canvas.
Task Details:
Import the random module and use it to generate a random number between 1 and 100.
Write a while loop that allows the user to enter a guess for the number.
Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.
Provide feedback based on the computed difference (e.g., "Very Hot" for close guesses).
The loop should continue until the user guesses the correct number.
Additional Notes:
The abs() function is a built-in Python function used to calculate the absolute value of a number. The absolute value of a number is its distance from zero on the number line, regardless of direction. For example, abs(-5) and abs(5) both return 5."""

def main():
    # importing the random module to generate a random number
    import random

    # Generate number between 1 and 100
    secret_number = random.randint(1, 100)

    print("Im thinking of a number between 1 and 100.")

    # Start the guessing loop and ask the user for their guess
    while True:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
        else:
            difference = abs(secret_number - guess)

            # Check if the guess is correct 
            if guess == secret_number:
                print("Congratulations! You've guessed the correct number.")
                break
            else:
                if difference <= 5:
                    print("Very Hot")
                elif difference <= 10:
                    print("Hot")
                elif difference <= 20:
                    print("Warm")
                elif difference <= 30:
                    print("Cold")
                else:   
                    print("Very Cold")


main()