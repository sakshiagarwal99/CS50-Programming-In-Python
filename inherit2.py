class Parent:

    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self,val,num): #child has own constructor so will not invoke Parent constructor
        self.__val = val

    def get_val(self):
        return self.__val

son = Child(100,10)
print("Parent Num:",son.get_num())
print("Child Val:",son.get_val())