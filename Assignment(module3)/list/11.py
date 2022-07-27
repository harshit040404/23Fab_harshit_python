a=input("Enter a string : ")

if len(a)>=2 and a[0]==a[-1]:
    print(a)
    print(len(a))
else:
    print("Enter valid number whose length is 2 or more than 2 \n and whose first and last letters are same")