def is_palindrome(s):
    return s == s[::-1]

string = input("Enter the string: ")
if is_palindrome(string):
    print("This is palindrom")
else:
    print("It is not palindrom")