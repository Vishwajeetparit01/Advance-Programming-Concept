students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students.append((name, marks))

students.sort(key=lambda x: x[1])

print("Students sorted by marks:")
for s in students:
    print(s)