"""
Project Plan:  Mexican Bowl or Burrito Ordering System
Student Name: Francesco Garcia
Course: ADD-100
Section: 004
Date: November 2025

Project Description:
Mexican bowl or burrito ordering system. 
Customer can view a menu, select an item, choose ingredients, calculate 
the total price into a receipt.txt file.
"""

# Class for menu items
class MenuItem:
    # Stores name and price of menu items
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(self.name, "- $", self.price)

# Class for a customer order
class Order:
    # Stores information about a customer's order
    def __init__(self, main_item, rice, beans, protein):
        self.main_item = main_item
        self.rice = rice
        self.beans = beans
        self.protein = protein
        self.extras = []
        self.total = 0.0

    def add_extra(self, extra):
        self.extras.append(extra)

    def calculate_total(self):
        self.total = self.main_item.price
        for item in self.extras:
            self.total = self.total + item.price

    def show_order(self):
        print("\n--- Your Order ---")
        print("Main Item:", self.main_item.name, "- $", self.main_item.price)
        print("Rice:", self.rice)
        print("Beans:", self.beans)
        print("Protein:", self.protein)
        if len(self.extras) > 0:
            print("Extras:")
            for item in self.extras:
                print("-", item.name, "- $", item.price)
        print("Total: $", self.total)

# Class for the ordering system 
class OrderSystem:
    def __init__(self):
        self.menu = []
        self.order = None

    def show_menu(self):
        print("\n--- Menu ---")
        for item in self.menu:
            item.print_info()

    def take_order(self, main_item, rice, beans, protein):
        self.order = Order(main_item, rice, beans, protein)

    def display_total(self):
        if self.order != None:
            self.order.calculate_total()
            self.order.show_order()
        else:
            print("No order has been placed.")

# Main program
def main():
    system = OrderSystem()

    # Create menu items
    bowl = MenuItem("Bowl", 10.50)
    burrito = MenuItem("Burrito", 11.50)
    guacamole = MenuItem("Guacamole", 2.0)
    extra_protein = MenuItem("Extra Protein", 3.0)
    system.menu = [bowl, burrito, guacamole, extra_protein]

    print("Welcome to Mexican Bowl and Burrito.")
    print("You can order a Bowl or Burrito along with ingredients.")

    # Choose main item
    while True:
        main_choice = input("Choose your main item (Bowl/Burrito): ").capitalize()
        if main_choice == "Bowl":
            main_item = bowl
            break
        elif main_choice == "Burrito":
            main_item = burrito
            break
        else:
            print("Invalid choice. Please type 'Bowl' or 'Burrito'.")

    # Choose ingredients
    rice = input("Choose your rice (White/Brown): ")
    beans = input("Choose your beans (Black/Pinto): ")

    protein = input("Choose your protein (Chicken/Beef/Vegetarian): ")

    # Validate protein choice
    while protein.capitalize() not in ["Chicken", "Beef", "Vegetarian"]:
        print("Invalid protein. Try again.")
        protein = input("Choose your protein (Chicken/Beef/Vegetarian): ")

    # Choose extras
    extras = []
    while True:
        more = input("Do you want extras? (yes/no): ").lower()
        if more == "no":
            break
        extra_choice = input("Type 'Guacamole' or 'Extra Protein': ").strip().lower()
        if extra_choice == "guacamole":
            extras.append(guacamole)
        elif extra_choice == "extra protein":
            extras.append(extra_protein)
        else:
            print("Invalid extra. Try again.")

    # Create order and add extras
    system.take_order(main_item, rice, beans, protein)
    for extra in extras:
        system.order.add_extra(extra)

    # Display order total
    system.display_total()

    # Save receipt to file
    try:
        with open("receipt.txt", "w") as receipt:
            receipt.write("--- Your Order ---\n")
            receipt.write(f"Main Item: {system.order.main_item.name} - ${system.order.main_item.price}\n")
            receipt.write(f"Rice: {system.order.rice}\n")
            receipt.write(f"Beans: {system.order.beans}\n")
            receipt.write(f"Protein: {system.order.protein}\n")
            if len(system.order.extras) > 0:
                receipt.write("Extras:\n")
                for item in system.order.extras:
                    receipt.write(f"- {item.name} - ${item.price}\n")
            receipt.write(f"Total: ${system.order.total}\n")

        print("Receipt has been written to receipt.txt")

    except Exception as e:
        print("There was an error writing the receipt file:", e)  

main()
