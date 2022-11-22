# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def get_number(input_string):
    '''
    Проверка ввода на число.
    '''
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число от 1 до 7: ')
        return get_number(input_string)

def day_of_the_week(day):
    '''
    Определение дня недели.
    :param day:
    print day of the week:
    '''
    if 1 > day or day > 7:
        print(f'{day} - такого дня недели не существует!')
        day_of_the_week(get_number('Введите число от 1 до 7: '))
    else:
        if day > 0 and day < 6:
            print(f'{day} - это будний день!')
        elif day > 5 and day < 8:
            print(f'{day} - это выходной день!')








    #     print('Такого дня недели не существует!')
    #     get_number('Введите число от 1 до 7: ')
    # elif 0 < day < 6:
    #     print('Это будний день!')
    # elif 1 > day > 8:
    #     print('Это выходной день!')
day_of_the_week(get_number('Введите число от 1 до 7: '))

