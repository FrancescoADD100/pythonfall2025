"""
Task:
Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.
Submission: Save your program in a .py file and upload it to GitHub.
Submit the GitHub link on Canvas. Include comments in your code explaining your logic.
"""

# List to store names
names = []

# Prompt user to enter five names
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

# Bubble sort names
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            # Swap if current name is greater than the next name
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True

# Sorted names
print("Sorted names:", names)

# Print names reverse sorted list
names.reverse()
print("Reversed sorted names:", names)
