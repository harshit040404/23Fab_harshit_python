from math import pi


def radian():
    print("Degree To Radian Conversion.....")
    d=float(input("\nEnter Degree of Angle : "))
    r=d*pi/180
    print(f"Radion of Degree is : {r}")

radian()