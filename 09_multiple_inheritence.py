class Car():
    def move(self):
        print("Car moves on road")
        
class Airplane():
    def move(self):
        print("Airplane moves in air")
        
class FlyingCar(Car,Airplane):
    def move(self):
        Car.move(self)
        Airplane.move(self)
        
flying_car=FlyingCar()
flying_car.move()