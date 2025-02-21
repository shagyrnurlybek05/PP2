import re

pattern = r"^a.*b$"

strings =["ab", "acb", "a123b", "aXYZb", "a_b", "a-b", "a long text with b", 
                "b", "abc", "ba", "a", "babab", "a!@#b", "aaab", "a...b"]

for i in strings:
    print(f"{i}: {bool(re.findall(pattern, i))}")