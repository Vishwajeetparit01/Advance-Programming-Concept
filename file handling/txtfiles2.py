
with open("file1.txt", "w") as f:
    text = input("Enter content for File 1: ")
    f.write(text)

with open("file2.txt", "w") as f:
    text = input("Enter content for File 2: ")
    f.write(text)


with open("file1.txt", "r") as f1:
    data1 = f1.read()

with open("file2.txt", "r") as f2:
    data2 = f2.read()

with open("file3.txt", "w") as f3:
    f3.write(data1 + "\n" + data2)

print("Both files merged into file3.txt")