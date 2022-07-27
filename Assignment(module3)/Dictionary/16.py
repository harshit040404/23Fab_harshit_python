dict1 = {'A' : [1,5,7,4],'B' : [2,5,7,10],'C' : [5,19,4,8],'D' : [5,7,2]}

print("The original dictionary is : " ,dict1)
  

res = list(sorted({ele for val in dict1.values() for ele in val}))
  
 
print("The unique values list is : " , res) 