import math

def area_of_parallelogram(length, height):
    return length * height

length = int(input("Enter the length of base: "))
height = int(input("Enter the height of parallelogram: "))

print(f"Expected output: {area_of_parallelogram(length, height)}")