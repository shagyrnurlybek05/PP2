def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def filter_primes(number_list):
    primes = [num for num in number_list if is_prime(num)]
    print(primes)

user_input = list(map(int, input("Enter numbers separated by spaces: ").split()))
filter_primes(user_input)