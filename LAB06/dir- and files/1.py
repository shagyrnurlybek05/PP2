import os

def list_contents(path: str):
    print("Directories:")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    
    print("\nFiles:")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    
    print("\nAll Directories and Files:")
    print(os.listdir(path))


specified_path = input("Enter the path: ")
list_contents(specified_path)
