class SomeString():
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper()) 

obj1 = SomeString()
obj1.getString()
obj1.printString()

# def getString():
#     str = input()
#     return str

# def printString(str):
#     print(str.upper())

# new_str = getString()
# printString(str)

