"""Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read. You need to print out all the data for each. You can create a method that prints everything or call each get function one at a time.
Additional Resources:

For this assignment, a class diagram is provided to help you understand the structure of the Person class. In future assignments, you will create your class diagrams using Microsoft Word and a simple table. Also, check out the accompanying video to learn more about accessors and mutators.

UML Class diagram
Person
- name: String
- address: String
- age: Integer
- phone: String
+ set_name(name)
+ set_address(address)
+ set_age(age)
+ set_phone(phone)
+ get_name()
+ get_address()
+ get_age()
+ get_phone()"""

class Person:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

# Getters
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone
    
    # Setters
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    
    # Information display method
def main():
    person1 = Person("Francesco", "878 Talismon Ave", 18, "815-1554")
    person2 = Person("Ada", "444 Club St", 25, "779-5078")
    person3 = Person("Alicia", "805 Pept St", 50, "847-9912")

    print(f"Name: {person1.get_name()}, Address: {person1.get_address()}, Age: {person1.get_age()}, Phone: {person1.get_phone()}")
    print(f"Name: {person2.get_name()}, Address: {person2.get_address()}, Age: {person2.get_age()}, Phone: {person2.get_phone()}")
    print(f"Name: {person3.get_name()}, Address: {person3.get_address()}, Age: {person3.get_age()}, Phone: {person3.get_phone()}")

main()


    

