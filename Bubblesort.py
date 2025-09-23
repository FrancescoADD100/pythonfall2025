"""
Task:
Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.
Submission:
Save your program in a .py file and upload it to GitHub. Submit the GitHub link on Canvas. Include comments in your code explaining your logic.
"""

# Prompt user to enter five names
n1 = input("Enter name 1: ")
n2 = input("Enter name 2: ")
n3 = input("Enter name 3: ")
n4 = input("Enter name 4: ")
n5 = input("Enter name 5: ")

# Bubble sort names
names = [n1, n2, n3, n4, n5]
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:

            # Swap if current names are greater than the next name
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True

# Sorted names
print("Sorted names:", names)

# Print names reverse sorted list
names.reverse()
print("Reversed sorted names:", names)
