def permutations(s,text=""):
    if len(s) == 0:
        print(text)
        return
    for i in range(len(s)):
        ch = s[i]
        left = s[:i]+s[i+1:]
        permutations(left,text + ch)
s= input()
permutations(s)