def has_33(numbers):
    for i in range(1,len(numbers)-1):
        if numbers[i]==3:
            if numbers[i-1]==3 or numbers[i+1]==3:
                return True
            return False
numbers = list(map(int,input().split()))
print(has_33(numbers))