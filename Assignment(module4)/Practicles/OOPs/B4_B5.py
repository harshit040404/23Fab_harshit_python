from math import pi


class circle :
    radius=float(input("Enter radius of a circle : "))

    def area(self):
        area = pi*self.radius*self.radius
        print(f"Area of Circle is : {area}")

    def parameter(self):
        para = 2*pi*self.radius
        print(f"PArameter of Circle is : {para}")


clr=circle()
clr.area()
clr.parameter()