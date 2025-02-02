def spy_games(numbers):
    zero = False
    second_zero=False
    for num in numbers:
        if num == '0' and not zero:
            zero = True
        elif num == '0' and zero:
            second_zero = True
        elif num == '0' and zero and second_zero:
            return True
    return False
numbers = input()
print(spy_games(numbers))
