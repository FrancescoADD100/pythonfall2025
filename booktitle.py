"""In this assignment, you will create a Python program that collects book titles from a user. Your program should use a while loop to prompt the user to enter a total of 10 book titles. Follow these steps to complete your assignment:

Set Up the Main Function: Write your program inside a main function. This is where your while loop will be implemented.
Collect Book Titles: Use a while loop to ask the customer to enter 10 book titles. Store these titles in a list.
Ensure proper capitalization: Use the title function to ensure that the first letter is capitalized before storing it in the list.
Create a Sorted List: Once all titles are collected, save them to a new list named books_sorted. This list should contain the titles in alphabetical order.
Display the Titles: Use a for loop to print each title from the sorted list on a separate line.
Test Your Program: Ensure your program runs correctly and meets all the requirements.
Upload to GitHub: Once tested, upload your program to GitHub.
Submit Your Work: Submit the link to your GitHub repository on Canvas.
Ensure your program is well-commented and follows the best practices for Python programming."""

def main(): 
    # Empty list to stor book titles
    book_titles = []
    count = 0

# Ask customer to enter 10 book titles and capitalize first letter
    while count < 10:
        book_title = input("Enter 10 book titles:")
        capitalized_title = book_title.title()
        count += 1
        book_titles.append(capitalized_title)
        
        # New list with sorted book titles
        books_sorted = sorted(book_titles)
        for title in books_sorted:
            print(title)

main()

