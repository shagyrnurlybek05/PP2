import re

pattern = r"\b[A-Z][a-z]+\b"

strings = ["Hello", "world", "Python", "AI", "MachineLearning", "Data_Science", 
            "Regex", "java", "C++", "Abc", "Test1", "X", "UpperCASE", "GoodMorning"]
for i in strings:
    print(f"{i}: {bool(re.findall(pattern, i))}")