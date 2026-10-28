a = set(input("Enter first book text: ").lower().split())
b = set(input("Enter second book text: ").lower().split())

print("Unique words in book 1:", a)
print("Unique words in book 2:", b)
print("Common words:", a & b)
print("Words only in book 1:", a - b)
print("Words only in book 2:", b - a)
print("Total unique words:", len(a | b))