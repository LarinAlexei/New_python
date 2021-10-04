"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.

"""

import timeit


# O(n) – линейная сложность
def my_func(num):
    values = []
    for i in range(len(num)):
        if num[i] % 2 == 0:
            values.append(i)
    return values


# O(n) – линейная сложность
def my_func_2(num):
    return [i for i, er in enumerate(num) if er % 2 == 0]


# запустим 1000
NUM = [er for er in range(1000)]

print(
    timeit.timeit(
        "my_func(NUM)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "my_func_2(NUM)",
        globals=globals(),
        number=1000))

# запустим 10000
NUM = [er for er in range(10000)]

print(
    timeit.timeit(
        "my_func(NUM)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "my_func_2(NUM)",
        globals=globals(),
        number=1000))

# запустим 100000
NUM = [er for er in range(100000)]

print(
    timeit.timeit(
        "my_func(NUM)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "my_func_2(NUM)",
        globals=globals(),
        number=1000))

# list comprehension отрабатывает быстрее.
