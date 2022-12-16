class Employee:
    company="Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning Dora!")
    @staticmethod
    def time():
        print("The time is 6AM in the morning")


Dora= Employee()
Dora.salary=10000000
Dora.getSalary()
Employee.getSalary(Dora)
Dora.greet()
Dora.time()