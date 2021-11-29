"""
1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
"""

# import Math

def square(a):
    p = a * 4
    s = a**2
    d = 2 ** a ** 0.5 # a * sqrt(2) OR import Math +
    #d = Math.sqrt(2 * a**2)
    return p, s, d

a = float(input())
print(square(a))
