class Person:
    country= "India"

    def takeBreath(self):
        print("I am breathing")
    
    def __init__(self):
        print("initializing Person...\n")

class Employee(Person):
    company= "Honda"
    
    def __init__(self):
        super().__init__()
        print("initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am employee so i am breathing")
   
class Programmer(Employee):
    company ="fiverr"

    def __init__(self):
        super().__init__()
        print("initializing Programmer...\n")
    def getSalary(self):
        print(f"No salary to programmers")
        
    def takeBreath(self):
        super().takeBreath()
        print("I am programmer so i am breathing")

p=Person()
p.takeBreath()
e=Employee()
e.salary=1000000
e.getSalary()
e.takeBreath()
e.__init__()
pr=Programmer()
pr.takeBreath()
pr.takeBreath()

