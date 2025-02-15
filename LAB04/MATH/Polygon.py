import math

def area_of_polygon(side, length):
    return (side * length**2) / (4 * math.tan(math.pi / side))

side = int(input("Enter the number of sides: "))
length = float(input("Enter the length of each side: "))

print(f"The area of the regular polygon is:{area_of_polygon(side, length)}")