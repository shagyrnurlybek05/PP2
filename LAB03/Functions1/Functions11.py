def palindrom(s):
    words = s.split()
    rwords = words[::-1]
    rsentence = " ".join(rwords)
    if s == rsentence:
        return True
    return False
s = input()
print(palindrom(s))
