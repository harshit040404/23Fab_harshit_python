import re

a= input ( " ENter a string :  " )

pattern_1="[A-Za-z0-9]"

x=re.findall(pattern_1,a)

if x :
    print("Pattern Matches")
else :
    print("match not found")