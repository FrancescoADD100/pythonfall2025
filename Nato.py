"""Your mission is to create a Python program that uses a dictionary to translate letters into the NATO Phonetic Alphabet. This program will ask users for a word and then spell it out using the NATO codes.

You will need to convert letters to upper case, here is an example:

      text = "Hello world"

      uppercase_text = text.upper()

      print(uppercase_text) 
Steps to Follow:
Create the NATO Phonetic Alphabet Dictionary:
Construct a dictionary in Python named NATO_ALPHABET (this is a global constant), where each key is a letter, and its value is the corresponding NATO phonetic term.
Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter to find and print the NATO phonetic term.
Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.
Test Your Program:
Test the program with various inputs, ensuring it works as expected.
Reference Table: NATO Phonetic Alphabet
NATO Phonetic Alphabet
Letter	Code Word
A	Alpha
B	Bravo
C	Charlie
D	Delta
E	Echo
F	Foxtrot
G	Golf
H	Hotel
I	India
J	Juliett
K	Kilo
L	Lima
M	Mike
N	November
O	Oscar
P	Papa
Q	Quebec
R	Romeo
S	Sierra
T	Tango
U	Uniform
V	Victor
W	Whiskey
X	X-ray
Y	Yankee
Z	Zulu
"""

"""NATO Phonetic Translator
This program asks the user for a word and then prints each letter
with its matching NATO phonetic alphabet code word."""

# NATO Phonetic Alphabet Dictionary
NATO_ALPHABET = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 
    'Y': 'Yankee', 'Z': 'Zulu'}

def spell_with_nato(word):
    # Helper function to spell a word using NATO phonetic alphabet

    # Iterate through each letter in the word
    for letter in word:

        # Only use alphabetic characters
        if letter in NATO_ALPHABET: # Only letters A-Z
            print(f"{letter}: {NATO_ALPHABET[letter]}")

def main():
    
    # Prompt user for a word
    word = input("Enter a word: ").upper()
    spell_with_nato(word) # Helper function

main()  

