def calc(x, o, y):
    x, y = float(x), float(y)
    if o == '+':
        return x + y
    if o == '-':
        return x - y
    if o == '*':
        return x * y
    if y == 0:
        return 'division by 0'
    if o == '/':
        return x / y

x, o, y = map(str, input().split())

print(calc(x, o, y))
