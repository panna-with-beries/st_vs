"""
5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
"""

def check(x, y):
    if x > y:
        s = 'х бiльше нiж у на ' + str(x - y)
    elif x < y:
        s = 'y бiльше нiж x на ' + str(y - x)
    else:
        s = 'х дорiвнює y'
    return s

x, y = input('enter x and y\n').split()
x, y = int(x), int(y)


print(check(x, y))