'''
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
'''
class LoginException(Exception):
    pass


def login_user(username, password, silent=False):

    db = [
        # name password
        ('Vika', 'password'),
        ('Jony', '1234'),
    ]

    for t in db:
        name, pw = t[0], t[1]
        if username == name and password == pw:
            return True
    if silent:
        return False
    raise LoginException("Error")

name = input('Enter name')
password = input('Enter password')
print(login_user(name, password))