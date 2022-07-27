import re

a=input("Enter a string : ")

us_pattern="[0-9]$"

x= re.findall(us_pattern,a)

if x:
    print("pattern matches")
else :
    print("error.....")