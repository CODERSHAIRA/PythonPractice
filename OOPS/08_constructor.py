class Employee:
    company="Google"

#constructor
    def __init__(self,name,salary,submit): 
        self.name=name
        self.salary=salary
        self.submit=submit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is{self.name}")
        print(f"The salary of the employee is{self.salary}")
        print(f"The submit of the employee is{self.submit}")
        
    def getSalary(self,signature):
        print(f"salary for this employee working in{self.company} is{self.salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("good morning, Dora")

    @staticmethod
    def time():
        print("The time is 4:14AM in the morning")

Dora = Employee("Dora",1000000,"Youtube")
Dora.getDetails()

