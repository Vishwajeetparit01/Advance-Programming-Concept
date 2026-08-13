project1 = set()
project2 = set()

n1 = int(input("Enter number of employees in Project 1: "))

for i in range(n1):
    name = input("Enter employee name: ")
    project1.add(name)

n2 = int(input("\nEnter number of employees in Project 2: "))

for i in range(n2):
    name = input("Enter employee name: ")
    project2.add(name)

both_projects = project1.intersection(project2)

only_project1 = project1.difference(project2)

only_project2 = project2.difference(project1)

all_employees = project1.union(project2)

print("\nEmployees working on both projects:", both_projects)
print("Employees working only on Project 1:", only_project1)
print("Employees working only on Project 2:", only_project2)
print("Total unique employees:", len(all_employees))
print("All unique employees:", all_employees)