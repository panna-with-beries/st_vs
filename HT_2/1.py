"""
1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.
"""

arr = [1, '2', 3, 4, 'fff', 5]
s = ''
for el in arr:
    s = s + str(el)

print(s)
