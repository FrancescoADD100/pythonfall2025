"""
Objective: Develop a program to manage ticket sales for an event.
Assignment Steps: Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.
"""

# List number of seats
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for seat in seats:
    print("available seats are 1-20")
    if seat:
        print(f"this seat is available {seat}")
    else:
        print("This seat is not available")
        number = 0
        while number >= 1 or number <= 20:
            number = int(input(f"You purchased number {seat}"))
            if number < 1 or number > 20:
                print(f"{number} is not available")
                seats.remove(number)
                for seat in seats:
                    print(seat)






