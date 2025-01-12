class Phone:

    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone): 
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("Inside SmartPhone Constructor")

ph = SmartPhone(1500,"Samsung",30,"Android",2)
print(ph.os)
print(ph.brand)