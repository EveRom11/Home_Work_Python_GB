# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

def monetochka(num):
    import random as rm
    list=[0]*num
    o,r=0,0
    for i in range(len(list)):
        list[i]=rm.randint(0,1)
        if list[i]==0:o+=1
        else:r+=1
    print(f'{list}\nСледует перевернуть всего', end=' ')
    print(o if o<r else r, 'монеток')


monetochka(15)