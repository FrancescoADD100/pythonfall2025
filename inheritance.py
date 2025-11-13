"""File 1: Write an Employee class with the following attributes:

Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class."""

# Employee class
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Getter and setter 
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    # Getter and setter 
    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        self.__number = number

# ProductionWorker class 
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    # Getter and setter
    def get_shift_number(self):
        return self.__shift_number
    
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    # Getter and setter
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate   
    
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

# Create instances of ProductionWorker
worker1 = ProductionWorker("Ada", 22, 1, 16.00)
worker2 = ProductionWorker("Jenny", 33, 2, 15.75)    

# Display worker info
print(f"Worker 1: {worker1.get_name()}, Number: {worker1.get_number()}, Shift: {worker1.get_shift_number()}, Pay Rate: ${worker1.get_hourly_pay_rate()}")
print(f"Worker 2: {worker2.get_name()}, Number: {worker2.get_number()}, Shift: {worker2.get_shift_number()}, Pay Rate: ${worker2.get_hourly_pay_rate()}")






