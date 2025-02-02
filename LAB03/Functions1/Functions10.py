def remove_duplicates(num):
    unique_nums = []
    for i in num:
        if i not in unique_nums:
            unique_nums.append(i)
    return unique_nums
numbers = list(map(int, input().split()))
print(remove_duplicates(numbers))