'''
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''

def good_login(name, password):
   if not((3 < len(name) <= 50) and (3 < len(password))):
      raise Exception("Мало символів")
   
   have_digit = False
   for chare in password:
      if chare.isdigit():
         have_digit = True
         break
   
   if not(have_digit):
      raise Exception("Пароль не містить цифр")
   
   have_ch = False
   for chare in '!:;,.*':
      if chare in password:
         have_ch = True
         break

   if not(have_ch):
      raise Exception("не містить ,!:;,*")
   return True


db = [
   # name password
   ('Vika', 'password'),
   ('Jony', '1234'),
   ('Jony Happy', 'asdasdf123123*'),
]

for t in db:
   name, pw = t[0], t[1]
   try:
      good_login(name, pw)
      print('Name : ' + name)
      print('Password : ' + pw)
      print('Status: OK')
      print('-' * 5)
   except Exception as r:
      print('Name : ' + name)
      print('Password : ' + pw)
      print('Status ' + str(r))
      print('-' * 5)
