# 
import string

with open("file.txt", "w") as file:
    file.write("Python is easy. Python is powerful. Python is used for programming.")

filename = "file.txt"

with open(filename, "r") as file:
    text = file.read()

text = text.lower()

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()

word_count = len(words)

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("Total number of words:", word_count)
print("\nTop 10 most frequent words:")

for word, count in sorted_words[:10]:
    print(word, ":", count)