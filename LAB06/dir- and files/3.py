import os

path = str(input("Enter the directory path: "))
if os.access(path, os.F_OK):
    print("The path exists!.")
    print("Files and Folders")
    list = os.listdir(path)
    for i in list:
        print(i)
else:
    print("The path does not exist! ")
