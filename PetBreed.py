"""Create the Pet Class:
Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
Implement get and set methods for each of these attributes.
Add a method called print_details that prints the details of the pet.
Create Instances:
Create three objects of the Pet class with different kinds, breeds, and names.

Call the print_details method for each object that you created

Demonstrate a Special Method or Function:
Choose three of the following and demonstrate its use with the Pet class instances:

__name__: Display the name of the class.
type(): Show the class used to instantiate a pet object.
__module__: Return the module name in which the Pet class is defined.
__bases__: Display the base classes of the Pet class (if any).
isinstance(): Check if an instance is of the Pet class."""

# Define Pet class
class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getter and setter 
    def get_kind(self):
        return self.__kind
    
    def set_kind(self, kind):
        self.__kind = kind

    # Getter and setter 
    def get_breed(self):
        return self.__breed
    
    def set_breed(self, breed):
        self.__breed = breed

    # Getter and setter 
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    # Method to print details 
    def print_details(self):
        print(f"Kind: {self.__kind}")
        print(f"Breed: {self.__breed}")
        print(f"Name: {self.__name}")

# Instances of Pet
pet1 = Pet("Dog", "Poodle", "Sadie")
pet2 = Pet("Hamster", "Syrian", "Kanye")    
pet3 = Pet("Cat", "Orange", "Garfield")

# Call print_details 
print("Pet 1 Details:")
pet1.print_details()
print("Pet 2 Details:")
pet2.print_details()
print("Pet 3 Details:")
pet3.print_details()

# Demonstrate special methods
print(Pet.__name__)
print(Pet.__module__)
print(Pet.__bases__)


















