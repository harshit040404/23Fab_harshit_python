# single inheritance

class father :
    bankbalance=0
    house=0

    def getdata(self):
        self.bankbalance=input("Enter Bank Balance : ")
        self.house=input("No. of House Own : ")

class son(father):
    def printdata(self):
        print("Total Bank balance Is  :",self.bankbalance)
        print("House Owned Is : ",self.house)

sn=son()
sn.getdata()
sn.printdata()

# multilevel inheritance

class grandfather:
    gold=0
    land=0

    def get_data(self):
        self.gold=input("Enter Gold : ")
        self.land=input("Enter Area of Land Own : ")

class father(grandfather) :
    bankb=0
    housep=0

    def getdata(self):
        self.bankb=input("Enter Bank Balance : ")
        self.housephousep=input("No. of House Own : ")

class son(father):
    def printdata(self):
        print("TOtal Gold Balance Is  : ",self.gold)
        print("Land Owned Is : ",self.land)
        print("Total Bank balance Is  :",self.bankb)
        print("House Owned Is : ",self.housep)

sn=son()
sn.get_data
sn.getdata()
sn.printdata()

#multiple inheritance

class python :
    ppon=0
    ppcom=0

    def ppdata(self):
        self.ppon=int(input("Enter No. of Python Projects Currently Working on : "))
        self.ppcom=int(input("Enter No. of Python Projects Completed :"))

class java :
    jpon=0
    jpcom=0

    def jpdata(self):
        self.jpon=int(input("Enter No. of Java Projects Currently Working on : "))
        self.jpcom=int(input("Enter No. of Java Projects Completed :"))

class infosolutions(python,java):
    
    def printdata(self):
        print(f"No. of Python Project Ongoing : {self.ppon}")
        print(f"No. of Java Project Ongoing : {self.jpon}")
        print(f"Python Project Completed : {self.ppcom}")
        print(f"Java Project Completed : {self.jpcom}")

info=infosolutions()
info.ppdata()
info.jpdata()
info.printdata()


'''The __init__method is the Python equivalent of the C++ constructor in an object-
oriented approach. The __init__function is called every time an object is created from a
class. The __init_method lets the class initialize the object's attributes and serves no other
purpose. It is only used within classes.'''

