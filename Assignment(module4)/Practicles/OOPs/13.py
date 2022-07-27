class numbers : 
    multiplier = 0

    def __init__(self):
        self.x = int(input("Enter Value Of X : "))
        self.y = int(input("Enter Value of Y : "))

        self.multiplier = self.x * self.y

        print(self.multiplier)


num = numbers()