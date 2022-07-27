a=str(input("Enter a string :"))


if len(a)<=6:
    print("Enter a string more than 1 length.")
elif len (a)>=8:
    if a[-3:]=='ing':
        a+='ly'
        print(a)
    else:
        a+='ing'
        print(a)
        