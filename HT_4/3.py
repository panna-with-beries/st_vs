"""
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.
"""


def is_prime(n):
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

n = int(input())
print(is_prime(n))
