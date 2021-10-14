"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??

"""

import timeit
import random


def bubble(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def best_bubble(lst_obj):
    n = 1
    flag = True
    while n < len(lst_obj) and flag:
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                flag = True
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


""" Параметры: """
len_arr = [10, 20, 50, 100, 200, 300]  # размер сортируемого массива
res_time = {'Len_arr': ('bs', 'best_bs', '%')}  # словарь для результатов замеров

""" Замеры: """
for len_i in len_arr:
    orig_list = [random.randint(-100, 100) for _ in range(len_i)]
    bs = timeit.timeit(
        "bubble(orig_list[:])",
        globals=globals(), number=1000)
    best_bs = timeit.timeit(
        "best_bubble(orig_list[:])",
        globals=globals(), number=1000)
    res_time[len_i] = (round(bs, 4), round(best_bs, 4),
                       round((best_bs / bs - 1) * 100, 2))
    print(f'-- При длине массива: {len_i}')
    print(f'Массив до сортировки: {orig_list}')
    print(f'Массив после сортировки bubble_sort или bs: {bubble(orig_list[:])}')
    print(f'Массив после  best_bubble_sort или best_bs: {best_bubble(orig_list[:])}')

""" результаты: """
for pos, item in enumerate(res_time.items()):
    print(f'{pos})  {item[0]}   {item[1][0]}  {item[1][1]}   {item[1][2]}')

"""
Было сделано:

1) Алгоритм сортирует массив по убыванию( поменяли знак ">" на "<" )
2) Добавили тригер flag, что позволяет выйти из while, в случае если перестановок значений не происходит.
3) Экономим время за счет отсутствия необходимости прохода по отсортированным значениям в конце массива.

Результат замера: 
0)  Len_arr   bs  best_bs   %
1)  10   0.0067  0.0044   -34.28
2)  20   0.0261  0.0185   -29.1
3)  50   0.1366  0.0874   -36.04
4)  100   0.5784  0.3859   -33.29
5)  200   2.3392  1.5524   -33.63
6)  300   5.3822  3.4461   -35.97


"""
