#

def attendance():
    print("Attendance Details:")

    with open("attendance.txt", "r") as file:
        for line in file:
            roll, name, present, total = line.strip().split(",")

            present = int(present)
            total = int(total)

            percentage = (present / total) * 100

            print(name, "-", percentage, "%")

            if percentage < 75:
                print("  Attendance below 75%")


with open("attendance.txt", "w") as file:
    file.write("101,Amit,80,100\n")
    file.write("102,Priya,65,100\n")
    file.write("103,Rahul,70,100\n")
    file.write("104,Neha,90,100\n")

attendance()