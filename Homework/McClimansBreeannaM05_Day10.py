"""
Reference Chapter 11 programming problem 1 p606.
Write an Employee class that keeps data attributes for the following pieces of information:
Employee name
Employee Number
Next, write a class named ProductionWorker that is a subclass of the Employee class.  
The ProductionWorker class should keep data attributes 
Shift Number (1 day or 2 night)
Hourly Pay Rate
Write appropriate Accessor and Mutator methods for each class. 
Once you have written the classes, write a program that creates an object of the ProductionWorker.  
Use the accessor methods to print out the object's full state.  
Then test the mutator methods doing an update of all attributes followed by a second print of the object's full revised state. 
"""

#Employee class
class Employee:
    def __init__(self, name, employee_number):
        self.__name = name
        self.__employee_number = employee_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_employee_number(self):
        return self.__employee_number

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

#ProductionWorker class, subclass of Employee
class ProductionWorker(Employee):
    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    #Accessor methods for shift number and hourly pay rate
    #Mutator methods for shift number and hourly pay rate
    def get_shift_number(self):
        return self.__shift_number

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

#Program to test the classes
def main():
    #Create a ProductionWorker object
    worker = ProductionWorker("Darrow O'Lykos", "12345", 1, 20.0)

    #Print the object's full state using accessor methods
    print("Original Employee Info:")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_employee_number())
    print("Shift Number:", worker.get_shift_number())
    print("Hourly Pay Rate:", worker.get_hourly_pay_rate())

    #Update all attributes using mutator methods
    worker.set_name("Darrow Au Augustus")
    worker.set_employee_number("67890")
    worker.set_shift_number(2)
    worker.set_hourly_pay_rate(40.0)

    #Print the object's full revised state using accessor methods
    print("\nRevised State:")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_employee_number())
    print("Shift Number:", worker.get_shift_number())
    print("Hourly Pay Rate:", worker.get_hourly_pay_rate())

if __name__ == "__main__":
    main()