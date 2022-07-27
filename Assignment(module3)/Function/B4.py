def palindrom():
    a=str(input("Enter A String : "))
    if a == a[::-1] :
        print("String Is Plaindrom")
    else :
        print("String Is Not Palindrome")

palindrom()