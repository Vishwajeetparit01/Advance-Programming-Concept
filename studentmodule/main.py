import student

marks = list(map(int, input("Enter 5 marks: ").split()))

t = student.total(marks)
p = student.percentage(marks)

print("Total:", t)
print("Percentage:", p)
print("Grade:", student.grade(p))