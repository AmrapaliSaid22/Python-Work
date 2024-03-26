# Que 1 Class and Object

'''class Car :
    def __init__(self, user_brand, user_model) :
        self.brand = user_brand
        self.model = user_model

car_brand = input("Enter a car brand :")
car_model = input("Enter a car model :")
my_car = Car(car_brand,car_model)
print(my_car.brand)
print(my_car.model) '''

#Que 2 Class method and self

'''class Car :
    def __init__(self, user_brand, user_model) :
        self.brand = user_brand
        self.model = user_model
    
    def full_name (self):
        return f"{self.brand} {self.model}"

car_brand = input("Enter a car brand :")
car_model = input("Enter a car model :")
my_car = Car(car_brand,car_model)
print(my_car.brand)
print(my_car.model) 

print(my_car.full_name()) '''

#Que 3 Inheritance

'''class Car :
    def __init__(self, user_brand, user_model) :
        self.brand = user_brand
        self.model = user_model
    
    def full_name (self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    
    def __init__(self, user_brand, user_model, user_battery_size):
        super().__init__(user_brand, user_model)
        self.battery_size = user_battery_size

my_tesla = ElectricCar("Tesla","Model S", "85KWH")
print(my_tesla.model)
print(my_tesla.full_name()) '''

#Que 4 Encapsulation

"""class Car :
    def __init__(self, user_brand, user_model) :
        self.brand = user_brand
        self.model = user_model
    
    def full_name (self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    
    def __init__(self, user_brand, user_model, user_battery_size):
        super().__init__(user_brand, user_model)
        self.battery_size = user_battery_size

my_tesla = ElectricCar("Tesla","Model S", "85KWH")
print(my_tesla.model)"""

#Que 5 Polymorphisum

'''class Car :
    def __init__(self, user_brand, user_model) :
        self.brand = user_brand
        self.model = user_model
    
    def full_name (self):
        return f"{self.brand} {self.model}"
    
    def fule_type(self):
        return "Petrol or Disel"

class ElectricCar(Car):
    
    def __init__(self, user_brand, user_model, user_battery_size):
        super().__init__(user_brand, user_model)
        self.battery_size = user_battery_size

    def fule_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla","Model S", "85KWH")
print(my_tesla.fule_type())

my_new_car = Car("Tata","Safari")
print(my_new_car.fule_type()) '''

#Que 6 static method

