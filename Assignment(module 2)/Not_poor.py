a=str(input("Enter a string:"))

b=a
c=d=0

c=a.find('not')
d=a.find('poor')


if(c>=0 and d>=0):
    b = b.replace(b[c:d+4],'good')
print(b)
