file_path = "file.txt"

with open(file_path, "r") as file:
    line_count = sum(1 for line in file)

print(f"Number of lines: {line_count}")