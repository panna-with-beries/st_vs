"""
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
"""

d = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3}
ans = {}
a = []

for i in d:
    if d[i] not in a:
        a.append(d[i])
        ans[i] = d[i]

print(ans)
