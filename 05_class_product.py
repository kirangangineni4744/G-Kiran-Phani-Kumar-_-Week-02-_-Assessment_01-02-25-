class Product():
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def check_availability(self,quantity):
        if quantity<=self.stock:
            print("Available")
        else:
            print("Not Available")

name=input("Enter the product name:")
price=int(input("Enter the product's price:"))
stock=int(input("Enter the stock available:"))

product=Product(name,price,stock)

quantity=int(input("Enter the quantity:"))
product.check_availability(quantity)