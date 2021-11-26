s = input()

def check(s):
    n = ''
    l = ''
    sumNums = 0
    
    for i in range(len(s)):
            if s[i].isalpha():
                l += s[i]
            elif s[i].isdigit():
                n += s[i]
                sumNums += int(s[i])
                
    if len(s) >=30 and len(s) <= 50:
        print('Довжина -', len(s))
        print('кiлькiсть букв -', len(l))
        print('кiлькiсть цифр -', len(n))
    elif len(s) < 30:
        print(sumNums)
        print(l)
    else:
        print('Nothing )')

check(s)
