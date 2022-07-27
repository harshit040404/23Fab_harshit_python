import re

a=input("Enter a string : ")
us_pattern="^[A-Ya-y]+[z]+[A-Ya-y]$"

x=re.findall(us_pattern,a)

if x:
    print("Pattern Matches")
else :
    print("Error")