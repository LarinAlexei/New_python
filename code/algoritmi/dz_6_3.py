"""
Задание 1.
Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!

"""
from memory_profiler import profile


@profile
def profile_recursion(*args):
    def recursion(cur_tnn):
        if cur_tnn == 0:
            return 0
        val = [i for i in range(10000)]
        summa_val = sum(val)
        return summa_val + recursion(cur_tnn - 1)

    res_summa = recursion(*args)
    return res_summa


if __name__ == '__main__':
    print(profile_recursion(100))

"""
Следовательно:
Чтобы недопустить повторный вызов profile, необходимо функцию с рекурсией обернуть в новую функцию и применить
к новой функции декоратор @profile.

Замер:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     18.9 MiB     18.9 MiB           1   @profile
    23                                         def profile_recurs(*args):
    24     57.4 MiB      0.1 MiB         102       def recursion(cur_n):
    25     57.4 MiB      0.0 MiB         101           if cur_n == 0:
    26     57.4 MiB      0.0 MiB           1               return 0
    27     57.4 MiB     38.5 MiB     1000300           new_val = [i for i in range(10000)]
    28     57.4 MiB      0.0 MiB         100           sum_new_val = sum(new_val)
    29     57.4 MiB  -1698.5 MiB         100           return sum_new_val + recursion(cur_n - 1)
    30                                         
    31     22.7 MiB    -34.8 MiB           1       res_sum = recursion(*args)
    32     22.7 MiB      0.0 MiB           1       return res_sum

"""
