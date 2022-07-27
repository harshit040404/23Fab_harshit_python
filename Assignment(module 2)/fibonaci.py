
a=int(input("Enter how many number want to print"))
N1=0
N2=1
count=0 

if a <= 0:
   print("Please enter a positive integer")
elif a == 1:
   print(f"Fibonacci sequence upto {a} is :{N1}")
else:
   print("Fibonacci sequence:")
   while count < a :
       print(N1)
       nth = N1 + N2