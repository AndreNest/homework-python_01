# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
#
# d = √ (х А – х В) 2 + (у А – у В) 2
import math
def get_number(input_string):
    '''
    Проверка ввода на число.
    '''
    try:
        num = float(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число: ')
        return get_number(input_string)
def coordinate(point_x1, point_y1, point_x2, point_y2):
    print(round(math.sqrt((point_x1 - point_x2) ** 2 + (point_y1 - point_y2) ** 2), 3))

coordinate(get_number('Введите точку x1: '),get_number('Введите точку y1: '),get_number('Введите точку x2: '),get_number('Введите точку y2: '))

