from abc import ABC,abstractmethod
import math

class IShape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(IShape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Circle(IShape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius*self.radius

length,width=map(float,input("Enter length and width of rectangle: ").split())
radius=float(input("Enter radius of circle: "))

rectangle=Rectangle(length,width)
circle=Circle(radius)

print(f"Rectangle area: {rectangle.area()}")
print(f"Circle area: {circle.area()}")
