from math import pi


print("Volume of A Cylinder")

r1=int(input("Enter radius R1 : "))
r2=int(input("Enter radius R2 : "))
h=int(input("Enter Height Of Cylinder : "))

volume=pi*h*(r1*r1 - r2*r2)

print("\nVolume of A Cylinder is : ",volume)


print("\nArea Of A Cylinder")

r= int(input("Enter Radius of a cylinder : "))

area = 2*pi*r*h+2*pi*r*r

print("\n Area Of A Cylinder is : ",area)