import os

try:
    file=open("data.txt","r")
    print(file.readlines())
except OSError:
    print("file is still opened")