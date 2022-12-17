class Person:
    country= "India"

    def takeBreak(self):
        print("I am breathing")

class Employee(Person):
    company= "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am employee so i am breathing")

class Programmer(Employee):
    company ="fiverr"
    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreak(self):
        print("I am programmer so i am breathing")

p=Person()
p.takeBreak()

e=Employee()

e.salary=1000000
e.getSalary()
e.takeBreak()
p=Programmer()
p.takeBreak()