import re

a=input ( " Enter String :  " )

x=re.findall("^a(0|b*)$",a)

if x:
    print("match found")
else:
    print("no match found")