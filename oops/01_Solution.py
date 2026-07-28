# Create a Car class with attributes like brand and model. Then create an instance of this class

class Car:
    def __init__(self,brand,model):
        self.__brand=brand #Private
        self.__model=model
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    # Encapulation
      # Getter
    def get_brand(self):
        return self.__brand

    # Setter
    def set_brand(self, brand):
        self.__brand = brand
    
    # Polymorphism
    
    def fuel_type(self):
        return "Petrol and Disel"
    
    @staticmethod
    def general_description():
        return "Car are means of transport"
    
    @property
    def model(self):
        return self.__model

      
    
my_car= Car("Toyota","Fortuner")
# my_car.model="def"

# print(my_car.__brand)
print(my_car.model)
# print(my_car.full_name())


#  Create an ElectricCar class that inherit from the Car class and has an additional attribute battery_size

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
     # Polymorphism
        
    def fuel_type(self):
        return "Electic charge"
        
        
# my_tesla= ElectricCar("Tesla","Model S","85kWh")
my_car.set_brand("BMW")
# print(my_tesla.fuel_type())

# print(my_car.fuel_type())


# print(my_car.general_description())
# print(Car.general_description())
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    pass


car = Car()








