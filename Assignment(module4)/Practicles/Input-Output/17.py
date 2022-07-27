import shutil

x=open("data.txt","r")
y=open("copy.txt","r+")

shutil.copyfile("data.txt","copy.txt")