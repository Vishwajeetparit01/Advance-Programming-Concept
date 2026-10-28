def student(name, roll, marks):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"
    return {"name": name, "roll": roll, "total": total,
            "percentage": percentage, "grade": grade}

name = input("Enter name: ")
roll = int(input("Enter roll number: "))
marks = list(map(int, input("Enter 5 marks: ").split()))

print(student(name, roll, marks))