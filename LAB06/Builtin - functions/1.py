import math

def multiply_list(numbers):
    return math.prod(numbers)

numbers = []
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = multiply_list(numbers)
print("Product of the list:", result)