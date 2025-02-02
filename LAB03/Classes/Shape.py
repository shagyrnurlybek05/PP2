class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        sqr = self.length * self.length
        print("S =",sqr)


obj = Square(5)
obj.area()

class Rectangle(Shape):
    def __init__(self, width, length):
        self.length = length
        self.width = width
    def area(self):
        rct = self.length * self.width
        print("S =", rct)

obj1 = Rectangle(5,10)
obj1.area()

