'''
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.

'''

from time import sleep

def svitlofor(color, a):
    for _ in range(a):
        print(color)
        sleep(1)


while True:
    svitlofor('Red        Green', 4)
    svitlofor('Yellow     Green', 2)
    svitlofor('Green      Red', 4)
    svitlofor('Yellow     Red', 2)