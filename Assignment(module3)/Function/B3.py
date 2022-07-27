def per_num():
    num=int(input("Enter A num : "))
    sum=0
    for i in range(1,num):
        if num%i==0 :
            sum = sum + i
    if sum==num :
        print("Num Is valid")
    else : 
        print("Num is Not valid")

per_num()