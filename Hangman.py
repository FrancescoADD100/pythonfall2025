"""
Change the WORD_LIST to include 15 different words on a subject of your choice (e.g., animals, food, movies, sports, etc.).
Finish the guessed_letters logic:
Before checking if the guessed letter is in the word, check if it is already in guessed_letters.
If it is, print a message like You already guessed that letter! and skip the rest of the loop using continue.
If it is not in the list, add it to guessed_letters and proceed with checking if it's in the word.
Display how many incorrect guesses they have left.
When You're Done
Run the game and test it with various word lengths
Try guessing the same letter more than once
Check that the game ends with 5 wrong guesses
Confirm that it congratulates you when you guess the word correctly
Hangman Start - Week 10 Strings Demo

This program begins a simple version of Hangman. You will finish it by:
- Adding a list to keep track of guessed letters
- Checking if the letter was already guessed BEFORE checking if it is in the word ( give them feedback)
- Changing the word list to 15 words on a subject of your choice
- Display how many incorrect guesses they have left 
- validate data entry (actual letter? only 1 letter?)
- use a try and except statement around data entry
"""

import random

WORD_LIST = ("PYTHON", "COBOL", "JAVASCRIPT", "BASIC", "CHICKEN", "CORN", "DOG", "TOMATO", "ZEBRA", "SOCCER", "PANDA", "BASKETBALL", "ELEPHANT", "GUITAR", "PIZZA")


def game(answer, display):
    wrong = 0
    right = 0

    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")

    guessed_letters = []

    while True:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        
        try:
            guess = input("Please enter a letter: ")
        except:
         print("Input error. Try again.")

        # validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE letter (A-Z).")
    
        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        else:
            guessed_letters.append(guess)

        bad_guess = True
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess
                right += 1
                bad_guess = False
        print(f"You have {guessed_letters}.")
        if bad_guess:
            print("Wrong!")
            wrong += 1
            if wrong == 5:
                print("You Lose!")
                print("The correct word was:", answer)
                break

        if right == len(answer):
            print("You Win!")
            print("The word was:", answer)
            break


def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)


main()
