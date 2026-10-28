
n = int(input("Enter number of students: "))

with open("attendance.txt", "w") as file:
    for i in range(n):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        present = int(input("Enter Present Days: "))
        total = int(input("Enter Total Days: "))

        file.write(roll + "," + name + "," + str(present) + "," + str(total) + "\n")


def attendance():
    print("\nAttendance Details:")

    with open("attendance.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            roll = data[0]
            name = data[1]
            present = int(data[2])
            total = int(data[3])

            percentage = (present / total) * 100

            print(name, ":", percentage, "%")

            if percentage < 75:
                print("Attendance below 75%")



attendance()