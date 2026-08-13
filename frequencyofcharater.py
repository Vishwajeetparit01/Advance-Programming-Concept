text = input("Enter a string: ")
ch = input("Enter the character to find: ")
count = 1
for c in text:
    if c == ch:
        count += 1

# Display the result
print("Number of occurrences:", count)