import re

text = "Hello, world. I'm study in KBTU!"
result = re.sub(r"[ ,.]",":", text)

print("Original string:",text)
print("After replacement:", result)
