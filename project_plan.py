"""
Project Plan: Chipotle Restaurant Ordering System
Student Name: Francesco Garcia
Course: Programming Logic (ADD-100)
Section: [Your Section]
Date: November 9, 2025

Project Description:
This project implements a Chipotle-style restaurant ordering system. 
Users can view a menu, select an item, choose ingredients, calculate 
the total price.
"""

"""
UML Class diagram
ChipotleSystem
- menu: list
- order: Order
+ show_menu()
+ take_order()
+ display_total()

Order
- main_item: MenuItem
- rice: String
- beans: String
- protein: String
- extras: list
- total: Float
+ add_extra(item)
+ calculate_total()
+ show_order()

MenuItem
- name: String
- price: Float
"""
# Class for menu items
class MenuItem:
    """Stores name and price of menu items"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(self.name, "- $", self.price)

# Class for a customer order
class Order:
    """Stores all information for a single order"""
    def __init__(self, main_item, rice, beans, protein):
        self.main_item = main_item
        self.rice = rice
        self.beans = beans
        self.protein = protein
        self.extras = []
        self.total = 0.0

    # Add extra item
    def add_extra(self, extra):
        self.extras.append(extra)

    # Calculate total price
    def calculate_total(self):
        self.total = self.main_item.price
        for item in self.extras:
            self.total = self.total + item.price

    # Show order details
    def show_order(self):
        print("Main Item:", self.main_item.name, "- $", self.main_item.price)
        print("Rice:", self.rice)
        print("Beans:", self.beans)
        print("Protein:", self.protein)
        if len(self.extras) > 0:
            print("Extras:")
            for item in self.extras:
                print("-", item.name, "- $", item.price)
        print("Total: $", self.total)

# Class for the Chipotle system
class ChipotleSystem:
    """Handles menu and the order"""
    def __init__(self):
        self.menu = []
        self.order = None

    # Show menu items
    def show_menu(self):
        print("Menu:")
        for i in range(len(self.menu)):
            print(i + 1, ".", self.menu[i].name, "- $", self.menu[i].price)

    # Take the main order
    def take_order(self, main_item, rice, beans, protein):
        self.order = Order(main_item, rice, beans, protein)

    # Display the order total
    def display_total(self):
        if self.order != None:
            self.order.calculate_total()
            self.order.show_order()
        else:
            print("No order has been placed.")

# Functions for user interaction
def directions():
    print("Welcome to Chipotle!")
    print("You can order a Bowl or Burrito and choose your ingredients.")

def get_main_item(system):
    system.show_menu()
    choice = int(input("Enter the number of your main item: "))
    return system.menu[choice - 1]

def get_rice():
    rice = input("Choose your rice (White/Brown): ")
    return rice

def get_beans():
    beans = input("Choose your beans (Black/Pinto): ")
    return beans

def get_protein():
    protein = input("Choose your protein (Chicken/Beef/Vegetarian): ")
    return protein

def get_extras(system):
    extras = []
    while True:
        more = input("Do you want extras? (yes/no): ").lower()
        if more == "no":
            break
        print("Extras available:")
        print("3. Guacamole - $2.0")
        print("4. Extra Protein - $3.0")
        choice = int(input("Enter the number of the extra item: "))
        extras.append(system.menu[choice - 1])
    return extras

# Main program
def main():
    system = ChipotleSystem()

    # Create menu items
    bowl = MenuItem("Bowl", 10.50)
    burrito = MenuItem("Burrito", 11.50)
    guacamole = MenuItem("Guacamole", 2.0)
    extra_protein = MenuItem("Extra Protein", 3.0)
    system.menu = [bowl, burrito, guacamole, extra_protein]

    directions()

    # Get user choices
    main_item = get_main_item(system)
    rice = get_rice()
    beans = get_beans()
    protein = get_protein()
    extras = get_extras(system)

    # Create order
    system.take_order(main_item, rice, beans, protein)
    for extra in extras:
        system.order.add_extra(extra)

    # Display final order
    system.display_total()

main()
