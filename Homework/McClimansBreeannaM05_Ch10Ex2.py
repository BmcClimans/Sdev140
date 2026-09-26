"""
Write a class named Car that has the following data attributes:                               
__year_model (for the car’s year model)                             
__make (for the make of the car)                             
__speed (for the car’s current speed)622                                                                              
The Car class should have an __init__ method that accepts the car’s year model and make as arguments. 
These values should be assigned to the object’s __year_model and __make data attributes. 
It should also assign 0 to the __speed data attribute.The class should also have the following methods:         
The accelerate method should add 5 to the speed data attribute each time it is called.                               
The brake method should subtract 5 from the speed data attribute each time it is called.       
The get_speed method should return the current speed.                                                               
Next, design a program that creates a Car object then calls the accelerate method five times. 
After each call to the accelerate method, get the current speed of the car and display it. 
Then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.
"""

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Accelerate the car by adding 5 to the speed.
    def accelerate(self):
        self.__speed += 5
   
    # Brake the car by subtracting 5 from the speed.
    def brake(self):
        self.__speed -= 5
    
    # Get the current speed of the car.
    def get_speed(self):
        return self.__speed

def main():
    #Create a car object
    car = Car(2023, "Subaru")

    #Accelerate the car five times and display the speed after each acceleration.
    print("Accelerating the car...")
    for count in range(5):
        car.accelerate()
        print(f"Current speed: {car.get_speed()}")
    
    #Brake the car five times and display the speed after each braking.
    print("Braking the car...")
    for _ in range(5):
        car.brake()
        print(f"Current speed: {car.get_speed()}")

if __name__ == "__main__":
    main()