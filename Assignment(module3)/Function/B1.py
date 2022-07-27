def factorial():
    n=int(input("enter a number to find factorial : "))
    fac=1
    if n<0 :
        print("no factorial for negative no.")
    else :
        for i in range(1,n+1):
            fac=fac*i
        print(f"Factorial of {n} is {fac}")

factorial()