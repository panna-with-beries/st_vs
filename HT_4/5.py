"""
5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""


def fibonacci(a):
    if a == 1:
        return []
    if a == 2:
        return [1, 1]
    if a == 0:
        return []
    fib = [1, 1, 2]
    i = 2
    while fib[i] + fib[i-1] < a:
        fib.append(fib[i] + fib[i-1])
        i += 1
    return fib

a = int(input())
print(fibonacci(a))
