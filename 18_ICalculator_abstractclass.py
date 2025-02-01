from abc import ABC,abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass

    @abstractmethod
    def subtract(self,a,b):
        pass

    @abstractmethod
    def multiply(self,a,b):
        pass

    @abstractmethod
    def divide(self,a,b):
        pass

class BasicCalculator(ICalculator):
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b if b!=0 else "Cannot divide by zero"

a,b=map(float,input("Enter two numbers: ").split())

calc=BasicCalculator()

print("Add:",calc.add(a,b))
print("Subtract:",calc.subtract(a,b))
print("Multiply:",calc.multiply(a,b))
print("Divide:",calc.divide(a,b))
