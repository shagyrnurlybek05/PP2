import re
pattern = r"^ab*$"
#Testing
strings = ["apple","a","abba","baba","hello","abc"]
for i in strings:
    print(f"{i}: {bool(re.findall(pattern, i))}")