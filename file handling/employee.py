
n = int(input("Enter number of employees: "))

with open("employees.txt", "w") as file:
    for i in range(n):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        file.write(emp_id + "," + name + "," + dept + "," + str(salary) + "\n")



def display():
    print("\nAll Employees:")

    with open("employees.txt", "r") as file:
        for line in file:
            print(line.strip())



def highest_salary():
    highest = 0
    employee = ""

    with open("employees.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            salary = float(data[3])

            if salary > highest:
                highest = salary
                employee = line.strip()

    print("\nHighest Paid Employee:")
    print(employee)


def average_salary():
    total = 0
    count = 0

    with open("employees.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            total += float(data[3])
            count += 1

    print("\nAverage Salary:", total / count)



def above_salary(amount):
    print("\nEmployees earning above", amount)

    with open("employees.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if float(data[3]) > amount:
                print(line.strip())



display()
highest_salary()
average_salary()

amount = float(input("\nEnter salary limit: "))
above_salary(amount)