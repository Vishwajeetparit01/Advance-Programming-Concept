
def display_records():
    with open("students.txt", "r") as file:
        print("\nStudent Records:")
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(roll, name, marks)


def highest_marks():
    highest = None

    with open("students.txt", "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            marks = int(marks)

            if highest is None or marks > highest[2]:
                highest = (roll, name, marks)

    print("\nHighest Marks:")
    print(highest[0], highest[1], highest[2])


def average_marks():
    total = 0
    count = 0

    with open("students.txt", "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            total += int(marks)
            count += 1

    print("\nAverage Marks:", total / count)


def above_80():
    print("\nStudents scoring more than 80:")

    with open("students.txt", "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")

            if int(marks) > 80:
                print(roll, name, marks)



with open("students.txt", "w") as file:
    file.write("101,Amit,85\n")
    file.write("102,Priya,92\n")
    file.write("103,Rahul,78\n")

display_records()
highest_marks()
average_marks()
above_80()
