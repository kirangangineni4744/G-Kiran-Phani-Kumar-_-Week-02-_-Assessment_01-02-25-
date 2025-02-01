class Vehicle:
    def __init__(self,company,model):
        self.company=company 
        self.model=model 

    def display(self):
        print(f"{self.company}'s new vehicle is model {self.model}")

class Car(Vehicle):
    def __init__(self,company,model,diesel_capacity):
        super().__init__(company,model)
        self.diesel_capacity=diesel_capacity
        
    def display1(self):
        print(f"Car's diesel capacity:{self.diesel_capacity}")
        
class Bike(Vehicle):
    def __init__(self,company,model,price):
        super().__init__(company,model)
        self.price=price
        
    def display2(self):
        print(f"Price of the bike:{self.price}")
        
class ElectricCar(Car):
    def __init__(self,company,model,battery_capacity):
        super().__init__(company,model,battery_capacity)
        self.battery_capacity=battery_capacity
        
    def display3(self):
        print(f"Battery capacity of the electric car:{self.battery_capacity}")
        
company=input("Enter the company's name:")
model=input("Enter the model name:")

vehicle=Vehicle(company,model)

diesel_capacity=int(input("Enter the diesel capacity of car:"))
car=Car(company,model,diesel_capacity)

speed=int(input("Enter the bike's speed:"))
bike=Bike(company,model,speed)

battery_capacity=int(input("Enter the battery capacity:"))
e_car=ElectricCar(company,model,battery_capacity)

vehicle.display()
car.display1()
bike.display2()
e_car.display3()