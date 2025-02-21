import re
pattern = r"^ab{2,3}"

strings = ["ab", "abb", "abbb", "abbbb", "a", "b", "aabb", "abbc", "abbba"]
for i in strings:
    print(f"{i}: {bool(re.findall(pattern, i))}")