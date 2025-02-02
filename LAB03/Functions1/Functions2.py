def fahren(fahrenheit):
    celsius = 5/9 * (fahrenheit - 32)
    return celsius
fahrenheit = float(input("Please enter the degree in fahrenheit:"))
celsius = fahren(fahrenheit)
print("The temperature in celsium:", celsius)
