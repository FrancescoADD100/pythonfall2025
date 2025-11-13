"""Assignment Details
Define a Pet Class:
Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
Set a default value for pet_type as "Dog".
Implement getter and setter methods for all properties.
Include a class variable vet_name set to the name of your veterinary office.
Add a method display_pet_info to print all details of the pet and owner.
Create Pet Objects:
Instantiate at least three pet objects with different details.
Show the use of setter methods for at least one pet object.
Implement Property Existence Check:
Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
Display Information:
Use display_pet_info to print details for each pet.
Show three examples of check_property being used on various properties and pets.
show two examples of display_pet_info on different instances of pet that you create"""

# Class definition 
class Pet:

# Class variable
    vet_name = "Doggy medical care" 

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
    
    # Getter and setter for owner_first_name
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type
    
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name

    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id
    
    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name
    
    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type
    
    # Method to display pet information
    def display_pet_info(self):
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary Office: {Pet.vet_name}")
    
    # Creating pet instances
pet1 = Pet("Alicia", "Walker", 1, "Sadie", "Dog")  
pet2 = Pet("Micheal", "Walker", 2, "Kanye", "Hamster")    
pet3 = Pet("Ada", "Montes", 3, "Garfield", "Cat")

    # Using setter method for pet2
pet2.set_pet_name("Kanye")
    
    # Function to check property existence
print(hasattr(pet1, "_Pet__owner_first_name"))  
print(hasattr(pet1, "_Pet__middle_name"))      
print(hasattr(pet2, "_Pet__pet_name"))         
print(hasattr(pet3, "_Pet__pet_type"))         

    # Displaying pet information
print("Pet 1 Information:")
pet1.display_pet_info()
print("Pet 2 Information:")
pet2.display_pet_info()
print("Pet 3 Information:")
pet3.display_pet_info()


    

    
    

    

    
    

    


    

    
    
    
    


    

    
    
    
        


    

    




    
    




    
    
    





    
    
    

    
    

    

    





        

    
    

 

