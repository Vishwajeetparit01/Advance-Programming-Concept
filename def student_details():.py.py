def display_student():
    print("\n--- STUDENT INFORMATION ---")

    student_name = input("Enter Student Name: ")
    student_class = input("Enter Class: ")
    phone = input("Enter Mobile Number: ")

    print("\nName:", student_name)
    print("Class:", student_class)
    print("Mobile Number:", phone)


def display_exam():
    print("\n--- EXAMINATION INFORMATION ---")

    semester_marks = []

    for sem in range(1, 7):
        marks = float(input("Enter marks for Semester " + str(sem) + ": "))
        semester_marks.append(marks)

    total = sum(semester_marks)
    average = total / 6

    print("\n--- SEMESTER MARKS ---")

    for sem in range(6):
        print("Semester", sem + 1, ":", semester_marks[sem])

    print("\nTotal Marks:", total)
    print("Cumulative Average:", round(average, 2))

    if average >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


print("Aarav")
print("Riya")
print("Kunal")

display_student()
display_exam()