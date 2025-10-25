"""At the end of this lesson, students will be able to:

Convert a character to its ASCII value using Python.
Convert an ASCII value back to a character.
Implement input validation using loops and error handling.
Step-by-Step Instructions
Start Your Python Script:
Open your Python environment and start a new script.
Use a main() function to organize your code.
Prompt for User Input:
Ask the user to enter a single character using input().
Validate the Input:
Ensure the user enters precisely one character.
Use len() to check input length.
Convert to ASCII Value:
Use the built-in function ord() to get the ASCII value.
Example:
ascii_value = ord(user_input)
Display the Result:
Print the ASCII value to the user.
Reverse Lookup:
Prompt the user to enter an ASCII value.
Ensure that the value is between 32 and 127.
Use a try-except block to handle invalid inputs.
Use the built-in function chr() to get the corresponding character.
Example:
character = chr(ascii_input)
Test Your Program:
Run your script and try various characters and ASCII values."""

def main():
         # Prompt for a single character input
    char = input("Enter a single character: ")
    while len(char) != 1:
        print("Invalid input. Please enter exactly one character.")
        char = input("Enter a single character: ")
    
    # Convert character to ASCII value
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}.")

    # Prompt for an ASCII value input
    while True:
        try:
            ascii_input = int(input("Enter an ASCII value (32–127): "))
            if 32 <= ascii_input <= 127:
                character = chr(ascii_input)
                print(f"The character for ASCII value {ascii_input} is '{character}'.")
                break
            else:
                print("Please enter a value between 32 and 127.")
        except ValueError:
            print("Invalid input. Please enter a numeric ASCII value.")
            
main()