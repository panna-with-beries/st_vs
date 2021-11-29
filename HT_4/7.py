"""
7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
"""


def same(el):
    dikt = {}
    for x in el:
        dikt.update({x: el.count(x)})
    print(dikt)

list_random = [1, 2, 'h', 'h', 'j', 'j', 2, 7]
same(list_random)