class rectangle :
    length=int(input("Enter Length Of Rectangle : "))
    width=int(input("Enter Width of Rectangle : "))
    area = length*width

    def print_data(self):
        print(f"Area of rectangle is : {self.area}")



rec=rectangle()
rec.print_data()