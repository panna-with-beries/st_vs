'''
2.Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
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



name = input('Enter name')
password = input('Enter password')
print(good_login(name, password))