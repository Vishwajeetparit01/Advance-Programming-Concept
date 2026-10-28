s=input("enter a string: ")

words =s.split()
longest = words[0]

for word in words:
    if len(words) > len(longest):
        longest = word 

print("longest word = ",longest)


