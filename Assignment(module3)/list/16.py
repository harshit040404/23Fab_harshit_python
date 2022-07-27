list=[1,2,5,7,7,9,56,7,9,96,55]
list1=[]

for x in list:
    if x not in list1 :
        list1.append(x)
print(list1)