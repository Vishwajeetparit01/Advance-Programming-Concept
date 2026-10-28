class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

name = input("Enter name: ")
age = int(input("Enter age: "))
emp_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))

e1 = Employee(name, age, emp_id, salary)

print("Employee object created successfully")
print(e1.name, e1.age, e1.emp_id, e1.salary)