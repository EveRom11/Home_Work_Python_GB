# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n= a1+ (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


def kol(a,d,n):
    res=a+(n-1)*d
    if n==0:return
    else: 
        kol(a,d,n-1)
        print(res)

kol(7,2,5)