'''
7. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
'''

def my_generator(array):
    while True:
        iterator = iter(array)
        try:
            while True:
                yield next(iterator)
        except StopIteration:
            True


for a in my_generator([1, 2, 3]):
    print(a)