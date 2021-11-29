"""
7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
"""


def same(a):
    b = set(a)
    return len(a) - len(b)

a = list(map(int, input().split()))
print(same(a))
