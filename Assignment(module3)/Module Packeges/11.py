#open("new.txt","x")
x=open("new.txt","r+")
x.write("\nthis is python file")
x.write("\nAssignment Advance qustion 11")
x.write("\nTask is to rad random line from file")

#to read random line

print(x.readlines()[2])