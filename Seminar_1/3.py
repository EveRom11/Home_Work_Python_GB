# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

def part(X,Y):
    import sys
    if 0<Y<sys.maxsize:
        print('Это первая четверть' if 0>X>-sys.maxsize else 'Это вторая четверть')
    elif 0>Y>-sys.maxsize:
        print('Это третья четверть' if 0>X>-sys.maxsize else 'Это четвертая четверть')
    else:
        print('Придерживайтесь условий задачи')
part(156744626,-6454512121596)