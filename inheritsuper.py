class Phone:

    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a phone")

class SmartPhone(Phone): 
    def buy(self):
        print("Buying a smartphone")
        super().buy() #super can only access parent methods and constructor and not attributes

ph = SmartPhone(1500,"Apple",30)
ph.buy() 