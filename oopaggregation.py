class Salary:

    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus
    

class Employee:

    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.salary = sal

    def total_salary(self):
        return self.salary.annual_salary()
    
sal = Salary(8000,5000)
emp1 = Employee("Sakshi",25,sal)
print(emp1.total_salary())