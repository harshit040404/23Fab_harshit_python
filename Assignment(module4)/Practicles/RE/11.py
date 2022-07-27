import re

a=input("Enter a string : ")
pattern="[a-z]+[_]+[a-z]"

x=re.findall(pattern,a)

if x:
    print("Pattern Matches")
else :
    print("Error")