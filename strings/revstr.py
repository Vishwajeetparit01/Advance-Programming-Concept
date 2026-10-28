# reverse the string withot reverse 

s = input("enter a string: ")
rev= ""
for ch in s:
    rev=ch + rev

print ("revere = ", rev)     

''' 
first take chracter then add is into rev then it will like eg
abc then 1st a then take fist ch is then rev= a 
then next char is b then rev = char + rev 
then rev = b + rev which is a == ba'''
