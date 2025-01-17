
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
###
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
##
text = "The best things in life are free!"
if "expensive" not in text:
  print("No, 'expensive' is NOT present.")
  ##
  texts = "The best things in life are free!"
if "free" in texts:
  print("Yes, 'free' is present.")


  ## Part 2(Slicing Strings)

  a = "Hello, World!"
print(a[2:5])
##
b = "Hello, World!"
print(b[-5:-2])

## Part 3 Modify Strings

d = "Hello, World!"
print(d.upper())

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello, World!"
print(a.replace("H", "J"))

## Part 4 String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)
##
x = "Hello"
y = "World"
z = x + " " + y
print(z)

## Part 5 Format - Strings

age = 36
text = f"My name is John, I am {age}"
print(text)

##
price = 59
text = f"The price is {price:.2f} dollars"
print(text)

### Part 5 Escape Characters

txt = "We are the so-called \"Vikings\" from the north."

