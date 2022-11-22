# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

def get_number(input_string):
    '''
    Проверка ввода на число.
    '''
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число: ')
        return get_number(input_string)

def coordinates(x):
    point = x
    return point

def quarter_coordinates(point_x, point_y):
    if point_x == 0  or point_y == 0:
        print("Вы ввели неверные значения!")
        quarter_coordinates(coordinates(get_number('Введите точку X: ')), coordinates(get_number('Введите точку Y: ')))
    elif point_x > 0 and point_y > 0:
        print(f'Введенные координаты: ({point_x}, {point_y}).\nЭто соотвесвует первой четверти.')
    elif point_x < 0 and point_y > 0:
        print(f'Введенные координаты: ({point_x}, {point_y}).\nЭто соотвесвует второй четверти.')
    elif point_x < 0 and point_y < 0:
        print(f'Введенные координаты: ({point_x}, {point_y}).\nЭто соотвесвует третьей четверти.')
    elif point_x > 0 and point_y < 0:
        print(f'Введенные координаты: ({point_x}, {point_y}).\nЭто соотвесвует четвертой четверти.')



quarter_coordinates(coordinates(get_number('Введите точку X: ')), coordinates(get_number('Введите точку Y: ')))

