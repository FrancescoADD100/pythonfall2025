"""
Objective: Develop a program to manage ticket sales for an event.
Assignment Steps: Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.
"""

# List of seats
seats = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("Welcome to Ticket Sales")

while True:
    print("Available seats:", seats)
    number = int(input("Enter the seat you want to purchase (0 to quit): "))
    
    if number == 0:
        print("Thank you for purchasing tickets")
        break
    if number < 1 or number > 20:
        print("That is not a valid seat. Pick 1-20")
    else:
        if number in seats:
            seats.remove(number)
            print("Seat", number, "Purchased")
        else:
            print("Seat already sold. Pick another")
    
    if len(seats) == 0:
        print("All seats are sold out")
        break