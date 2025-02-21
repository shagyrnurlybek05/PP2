import re

pattern = r"\b[a-z]+_[a-z]+\b"

strings = ["hello_world", "test_case", "Python_code", "snake_case_style",
           "no_underscore", "ABC_def", "_underscore", "lower_case1", "hello__world"]

for i in strings:
    print(f"{i}: {bool(re.findall(pattern, i))}")