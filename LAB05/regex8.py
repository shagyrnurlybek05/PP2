import re

pattern = r"[A-Z][^A-Z]*"

text = "HelloWorldThisIsPython"

result = re.findall(pattern, text)

print("Original string:", text)
print("After split:", result)
