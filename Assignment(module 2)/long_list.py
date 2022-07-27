a=['bus','train','scooter','bike','car']

longlist = len(a[0])
temp = a[0]

for i in a:
    if len(i) > longlist:
        longlist = len(i)
        temp = i

print(f"word with long length is : {temp}")