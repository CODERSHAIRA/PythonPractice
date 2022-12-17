class Employee:
    salary=500
    increment=200
    @property
    def salaryAfterIncreament(self):
        return self.salary +self.increment 

e = Employee()
print(e.salaryAfterIncreament)
