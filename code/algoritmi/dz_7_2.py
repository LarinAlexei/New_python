"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]

"""

import timeit
import random
import operator


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


def merge_sort_v2(lst_obj, compare=operator.lt):
    if len(lst_obj) < 2:
        return lst_obj[:]
    else:
        middle = int(len(lst_obj) / 2)
        left = merge_sort_v2(lst_obj[:middle], compare)
        right = merge_sort_v2(lst_obj[middle:], compare)
        return merge_v2(left, right, compare)


def merge_v2(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


""" Параметр замера: """
len_arr = [10, 20, 50, 100, 200]  # размер сортируемого массива
res_time = {'Len_arr': ('ms', 'ms2', '%')}  # словарь для результатов замеров

for len_i in len_arr:
    orig_list = [random.random() * 49.99 for _ in range(len_i)]
    ms = timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(), number=1000)
    ms2 = timeit.timeit(
        "merge_sort_v2(orig_list[:])",
        globals=globals(), number=1000)
    res_time[len_i] = (round(ms, 4), round(ms2, 4),
                       round((ms2 / ms - 1) * 100, 2))
    print(f'-- При длине массива: {len_i} ')
    print(f'Массив до сортировки: {orig_list}')
    print(f'Массив после сортировки merge_sort или ms: {merge_sort(orig_list[:])}')
    print(f'Массив после сортировки merge_sort_v2 или ms2: {merge_sort_v2(orig_list[:])}')

""" Выводим результаты: """
for pos, item in enumerate(res_time.items()):
    print(f'{pos})  {item[0]}   {item[1][0]}  {item[1][1]}   {item[1][2]}')


"""

Было сделано:
1) Создан массив который задает рандомные числа от 0 до 50.
2) Новый вариант реализации, где используется библиотека operator для выполнения сравнения.


Вывод из проделаной работы:
 Результаты замеров показали, что базовая функция ms работает быстрее второго варианта. 
Считаю что использование библиотеки operator является избыточным, 
что приводит к потерям времени, подтверждения этому замеры приведенные ниже:

0)  Len_arr   ms  ms2   %
1)  10   0.009  0.0117   30.33
2)  20   0.0209  0.0259   24.07
3)  50   0.0579  0.074   27.8
4)  100   0.1397  0.1705   22.1
5)  200   0.2881  0.3599   24.94

"""
