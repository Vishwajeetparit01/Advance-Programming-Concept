# count uppercase & lower case letters

s = input("enter a string: ")
upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower +=1

print("upercase = ",upper)
print("lowecase = ",lower)   
