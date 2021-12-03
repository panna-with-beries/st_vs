'''
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
'''
def range_me (st, sp=0, stp=1):
    if sp == 0:
        st, sp = 0, st
    if stp == 0:
        raise ValueError()
    if stp > 0:
        while st < sp:
            yield st
            st = st + stp
    else:
        while st > sp:
            st = st + stp
for i in range_me (3):
    print (i)

print (list(range_me(3)))
print (list(range_me(3,12)))
print (list(range_me(3,12,3)))
print (list(range_me(15,3,0)))