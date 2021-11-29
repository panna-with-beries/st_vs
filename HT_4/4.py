"""
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона
"""


def prime_list(a, b):
    p = []
    for i in range(a, b+1):
        flag = True
        if i == 0:
            continue
        if i == 1:
            p.append(i)
            continue
        if i == 2:
            p.append(i)
            continue
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag == True:
            p.append(i)
    return p
a, b = map(int, input().split())
print(' '.join(map(str, prime_list(a, b))))
