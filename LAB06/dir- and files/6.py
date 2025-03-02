import string

for text in string.ascii_uppercase:
        file_name = f"{text}.txt"
        try:
            with open(file_name, "x") as file:
                file.write(f"This is file {file_name}\n")
            print(f"Created file: {file_name}")
        except FileExistsError:
            print(f"File {file_name} already exists. Skipping creation.")