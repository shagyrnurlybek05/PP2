class Point():
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    def show(self):
        print("(", self.x, ",", self.y, ")")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, new): # new - the object class of Point
        dx = self.x - new.x
        dy = self.y - new.y
        distance = (dx**2 + dy**2)** 0.5
        print("Distance:",distance)


# Create first point
X1 = input("X coordinate is:")
Y1 = input("Y coordinate is:")
obj1 = Point(X1, Y1)
obj1.show()


# Update coordinates first point for obj1
new_x = int(input("New_X coordinate is: "))
new_y = int(input("New_Y coordinate is: "))
obj1.move(new_x, new_y)
obj1.show()


# Create second point for calculation distance
X2 = input("X coordinate for second point:")
Y2 = input("Y coordinate for second point:")
obj2 = Point(X2,Y2)
obj2.show()


# Calculate dimension between obj1 and obj2
obj1.dist(obj2)