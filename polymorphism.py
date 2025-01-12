class Phone:

    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone): #Inheritance: smartphone is the child class that inherits from parent class phone

    def buy(self):
        print("Buying a smartphone")

ph = SmartPhone(1500,"Apple",30)
ph.buy() #Method Overriding --> Polymorphism

# Polymorphism has three types
# Method Overriding
# Method Overloading
# Operator Overloading