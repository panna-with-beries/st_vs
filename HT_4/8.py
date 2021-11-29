"""
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
"""

def shift(a, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            a.append(a.pop(0))
    else:
        for i in range(steps):
            a.insert(0, a.pop())
    return a
 
 
a = list(map(int, input().split()))
step = int(input())
print(' '.join(map(str, shift(a, step))))
