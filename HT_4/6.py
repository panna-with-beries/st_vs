"""
6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""


a = float(input())
if a > 0:
    a **= 2
elif a < 0:
    a += 100
print(a)
