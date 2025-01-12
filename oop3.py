class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def change_profile(self,new_name,new_city,new_state,new_pincode):
        self.name = new_name
        self.address.change_address(new_city,new_state,new_pincode)

class Address:

    def __init__(self,city,state,pincode):
        self.city = city
        self.state = state
        self.pincode = pincode

    def change_address(self,new_city,new_state,new_pincode):
        self.city = new_city
        self.state = new_state
        self.pincode = new_pincode

add = Address("Pune","Maharashtra",411048)
cust = Customer("Sakshi","Female",add)
cust.change_profile("Priya","Mumbai","Maharashtra",43076)
print(cust.address.pincode)