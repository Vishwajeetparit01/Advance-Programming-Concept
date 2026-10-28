a = set(input("Enter employees in project 1: ").split())
b = set(input("Enter employees in project 2: ").split())

print("Employees in both projects:", a & b)
print("Employees only in project 1:", a - b)
print("Employees only in project 2:", b - a)
print("All unique employees:", a | b)