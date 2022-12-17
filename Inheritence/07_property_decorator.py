class Employee:
    company ="Bharat Gas"
    salary=38762746
    salarybonus =5000

    @property
    def totalSalary(self):
        return self.salary +self.salarybonus
    
    @totalSalary.setter
    def totalSalary(self , val):
        self.salarybonus = val -self.salary
        
e=Employee()
print(e.totalSalary)
e.totalSalary=2364623
print(e.salary)
print(e.salarybonus)



