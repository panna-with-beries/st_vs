"""
4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
"""

def week1(week):
    if week  in ['1']:
        return 'Monday'
    elif week  in ['2']:
        return 'Tuesday'
    elif week  in ['3']:
        return 'Wednesday'
    elif week  in ['4']:
        return 'Thursday'
    elif week in ['5']:
        return 'Friday'
    elif week in ['6']:
        return 'Saturday'
    elif week in ['7']:
        return 'Sunday'
    else:
        return 'Not found'


def rest2(rest):
    if rest in ['1', '2', '3', '4', '5']:
        return 'Work day'
    elif rest in ['6', '7']:
        return 'Rest day'
    else:
        return 'Not found'


def lessons3 (less):
    if less in ['1', '2', '5', '6', '7']:
        return 'Dont have a lessons'
    elif less in ['3', '4']:
        return 'Study at school'
    else:
        return 'Not found'


def result4 (result):
    res1 = week1(result)
    res2 = rest2(result)
    res3 = lessons3(result)
    print(res1, res2, res3, sep=', ')


result4(input('Please, enter number of the day - '))
