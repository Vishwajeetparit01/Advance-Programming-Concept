# palindrome check 

s = input("enter a string: ")
rev=""

for ch in s:
    rev=ch + rev

if s==rev:
  print("palindrome")
else:
  print("not palindrome")

  '''  1st make the thebstring rev then cjcek given is = to rev then it is palindrome '''