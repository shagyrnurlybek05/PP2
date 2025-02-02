
def mass(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = float(input())
ounces = mass(grams)
print(ounces)

def fahren(fahrenheit):
    celsius = 5/9 * (fahrenheit - 32)
    return celsius
fahrenheit = float(input("Please enter the degree in fahrenheit:"))
celsius = fahren(fahrenheit)
print("The temperature in celsium:", celsius)

