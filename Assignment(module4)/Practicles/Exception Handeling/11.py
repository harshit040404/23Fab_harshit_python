try :
    age=int(input("Enter your Age : "))

except ValueError :
    print(ValueError)

else :
    if age >= 18 :
        print("Eligible to Vote")
    else :
        print("Not Eligible to Vote")