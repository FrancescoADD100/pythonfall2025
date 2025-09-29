"""
Objective: Develop a program to manage ticket sales for an event.
Assignment Steps:
1. Create a list representing 20 seats, numbered 1 to 20.
2. Display the list of available seats to the customer.
3. Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
4. Remove the selected seat from the list of available seats and display the updated list.
5. If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
6. Ensure the program gracefully handles all scenarios and is user-friendly.
"""


# List of seats
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Welcome to Ticket Sales")

# Loop until user chooses to quit or all seats are sold
while True:

      # Display current list of available seats
    print("Available seats:", seats)
    
    # Prompt user for seat number
    number = int(input("Enter the seat you want to purchase (0 to quit): "))
    
    # End program if user enters 0
    if number == 0:
        print("Thank you for purchasing tickets")
        break

    # Accept seat if available
    if number < 1 or number > 20:
        print("That is not a valid seat. Pick 1-20")
    else:

        # If seat is available, remove it and confirm purchase
        if number in seats:
            seats.remove(number)
            print("Seat", number, "Purchased")
        else:

            # If seat is already sold, prompt to pick another
            print("Seat already sold. Pick another")
    
    # If all seats are sold, end program
    if len(seats) == 0:
        print("All seats are sold out")
        break