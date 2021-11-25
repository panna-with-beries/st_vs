"""
7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""

def calc(x, o, y):
    x, y = int(x), int(y)
    if o == '+':
        return x + y
    if o == '-':
        return x - y
    if o == '*':
        return x * y
    if o == '/':
        if y == 0:
            return 'div 0'
        return x / y
    return 'No fined operation'


x, o, y = input().split()

print(calc(x, o, y))
