class Shape():
    def area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side=side  
    def area(self):
        return self.side*self.side

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height

side=int(input("Enter side length:"))
square=Square(side)

base=int(input("Enter base length:"))
height=int(input("Enter the height length:"))
triangle=Triangle(base,height)

print(f"Square Area: {square.area()}")
print(f"Triangle Area: {triangle.area()}")