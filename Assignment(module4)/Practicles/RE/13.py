import re

a=input("Enter string : ")

us_pattern="^[0-9]$"

x=re.split(us_pattern,a)

print(x)