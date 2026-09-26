"""
    Write a class named Person with data attributes for a person’s name, address, and telephone number. 
    Next, write a class named Customer that is a subclass of the Person class. 
    The Customer class should have a data attribute for a customer number, 
    and a Boolean data attribute indicating whether the customer wishes to be on a mailing list. 
    Demonstrate an instance of the Customer class in a simple program.
"""

class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    #Accessor methods for the Person class
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone

#Create the Customer class as a subclass of the Person class
class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, on_mailing_list):
        #init Person attributes
        super().__init__(name, address, telephone)
        #init Customer attributes
        self.__customer_number = customer_number
        self.__on_mailing_list = on_mailing_list

    #Accessor methods for the Customer class
    def get_customer_number(self):
        return self.__customer_number

    def is_on_mailing_list(self):
        return self.__on_mailing_list

def main():
    #create Customer object and display its information
    customer = Customer("Moraine Damodred", "123 White Tower Rd", "765-1234", "C12345", True)
    print(f"Name: {customer.get_name()}")
    print(f"Address: {customer.get_address()}")
    print(f"Telephone: {customer.get_telephone()}")
    print(f"Customer Number: {customer.get_customer_number()}")
    print(f"On Mailing List: {customer.is_on_mailing_list()}")

if __name__ == "__main__":
    main()  