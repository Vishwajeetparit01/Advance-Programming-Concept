students = []
grades = []

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))

        students.append(name)
        grades.append(grade)

        print("Student added successfully.")

    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            index = students.index(name)

            grade = float(input("Enter new grade: "))
            grades[index] = grade

            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == 3:
        name = input("Enter student name: ")

        if name in students:
            index = students.index(name)

            students.pop(index)
            grades.pop(index)

            print("Student removed successfully.")
        else:
            print("Student not found.")

    elif choice == 4:
        if len(grades) > 0:
            average = sum(grades) / len(grades)
            print("Average grade =", average)
        else:
            print("No grades available.")

    elif choice == 5:
        if len(students) > 0:
            print("\nStudent Details:")
            for i in range(len(students)):
                print(students[i], ":", grades[i])
        else:
            print("No students available.")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")