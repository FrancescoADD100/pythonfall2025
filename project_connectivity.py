"""
Project Plan: Chipotle Ordering System
Student Name: Francesco Garcia
Course: ADD-100
Section: 004
Date: November 2025

Project Description:
Mexican bowl or burrito ordering system. 
Customer can view a menu, select an item, choose ingredients, calculate 
the total price.
"""

# Class stubs

class MenuItem:
    # Represents a menu item 
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        # Prints the menu item information
        

class Order:
        # Represents customer's order
    def __init__(self, main_item, rice, beans, protein):
        self.main_item = main_item
        self.rice = rice
        self.beans = beans
        self.protein = protein
        self.extras = []
        self.total = 0.0

    def add_extra(self, extra):
        # Adds an extra item to the order
        

    def calculate_total(self):
        # Calculates total price of the order
        

    def show_order(self):
        # Displays the order details
        

class ChipotleSystem:
    # Represents the ordering system
    def __init__(self):
        self.menu = []
        self.order = None

    def show_menu(self):
        # Displays all items in the menu
        

    def take_order(self, main_item, rice, beans, protein):
        # Creates a new order
        

    def display_total(self):
        # Displays total price of the order
        

# Function stubs

def directions():
    # Prints welcome message and instructions
    

def get_main_item():
    # Select main item (Bowl or Burrito)
    

def get_rice():
    # Select rice type
    

def get_beans():
    # Select beans type
    

def get_protein():
    # Select protein type
    

def get_extras():
    # Select extra items
    

# Connectivity Check - main program
def main():
    # Create system
    system = ChipotleSystem()

    # Create sample menu items
    bowl = MenuItem("Bowl", 10.50)
    burrito = MenuItem("Burrito", 11.50)
    
    system.menu = [bowl, burrito]

    # Example of choosing a main item
    main_item = bowl
    rice = "White"
    beans = "Black"
    protein = "Chicken"
    extras = "guacamole"

    # Take order
    system.take_order(main_item, rice, beans, protein)
    for extra in extras:
        system.order.add_extra(extra)

    # Calculate and show total
    system.display_total()

    # Short summary
print("\n--- Connectivity Summary ---")
print("Menu Items:")
for item in system.menu:
    print("-", item.name, "$", item.price)

print("\nOrder Details:")
print("Main Item:", system.order.main_item.name)
print("Rice:", system.order.rice)
print("Beans:", system.order.beans)
print("Protein:", system.order.protein)

if len(system.order.extras) > 0:
    print("Extras:")
    for extra in system.order.extras:
        print("-", extra.name)

print("Total:", system.order.total)

main()
