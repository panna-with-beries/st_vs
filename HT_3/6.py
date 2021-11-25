"""
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""

s = input()
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def check(s):
    n = ''
    letters= ''
    sumNums = 0
    
    for i in range(len(s)):
        if s[i] not in nums:
            letters += s[i]
        else:
            n += s[i]
            sumNums += int(s[i])
                
    if len(s) >= 30 and len(s) <= 50:
        print('Довжина -', len(s))
        print('кiлькiсть букв -', len(letters))
        print('кiлькiсть цифр -', len(n))
    elif len(s) < 30:
        print(sumNums)
        print(letters)
    else:
        # print('Nothing )')
        print(s[::-1])


check(s)
