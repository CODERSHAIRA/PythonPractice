class Employee:
    company ="Google"

Shinchan= Employee()
Doraemon= Employee()

print(Shinchan.company)
print(Doraemon.company)

Employee.company="Microsoft"

print(Shinchan.company)
print(Doraemon.company)