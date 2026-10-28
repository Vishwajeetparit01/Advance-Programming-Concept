
s=input("enter a string: ")
ch=input("enter a character: ")

count = 0

for i in s:
    if i==ch:
        count =count +1
print("frequency = ", count)