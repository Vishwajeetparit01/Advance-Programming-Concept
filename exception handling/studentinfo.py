try:
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    print("Name:", name)
    print("Roll number:", roll)
    print("Marks:", marks)
except ValueError:
    print("Please enter valid numeric values")