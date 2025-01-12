class Atm:

    __counter = 1

    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.__counter
        Atm.__counter += 1
        self.__menu()

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new_counter):
        if isinstance (new_counter,int):
            Atm.__counter = new_counter
        else:
            print("Not Allowed") 

    @property
    def pin(self):
        return self.__pin
    
    @pin.setter
    def pin(self,new_pin):
        if not isinstance(new_pin,str):
            raise TypeError("Pin should be string")
        else:
            self.__pin = new_pin
    
    @property
    def balance(self):
        return self.__balance

    def __menu(self):
        user_input = input(""" 
                Hello, How would you like to proceed?
                Enter 1 to Create Pin
                Enter 2 to Deposit
                Enter 3 to Withdraw
                Enter 4 to Check Balance
                Enter 5 to Exit """)
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("GoodBye")

    def create_pin(self):
        self.__pin = input("Enter Pin ")
        print("Pin Created Successfully")
    
    def deposit(self):
        user_pin = input("Enter your pin ")
        if self.__pin == user_pin:
            amount = int(input("Enter Amount You Want to Deposit "))
            self.__balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")

    def withdraw(self):
        user_pin = input("Enter your pin ")
        if self.__pin == user_pin:
            amount = int(input("Enter Amount You Want to Withdraw "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdraw Successful")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid Pin")

    def check_balance(self):
        user_pin = input("Enter your pin ")
        if self.__pin == user_pin:
            print(self.__balance)
        else:
            print("Invalid Pin")