from math import sqrt, floor


def is_prime(number):
    if number <= 1:
        return False

    if number == 2:
        return True

    value = floor(sqrt(number))
    for i in range(2, value + 1):
        if number % i == 0:
            return False
    return True


def get_primes(numbers):
    for x in numbers:
        if is_prime(x):
            yield x


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
