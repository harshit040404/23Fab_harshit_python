a=input("enter value:")
  
if a.isdecimal():
    print("its integer")
elif a.isalpha():
    print("its stirng")
else:
    print("neither int nor string")
