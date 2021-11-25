"""
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
"""

def season(num):
    if num in ['12', '1', '2']:
        return 'Winter'
    elif num in ['3', '4', '5']:
        return 'Spring'
    elif num in ['6', '7', '8']:
        return 'Summer'
    elif num in ['9', '10', '11']:
        return 'Autumn'
    else:
        return 'Not found'

c = input('You can write the number of mounth ')
print(season(c))

