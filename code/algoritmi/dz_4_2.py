"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым.

"""

from timeit import timeit
from random import randint

# from copy import copy

num_x100 = randint(10000, 1000000)
num_x1000 = randint(1000000, 10000000)
num_x10000 = randint(100000000, 10000000000000)


# Без мемоизации
def recursive(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive(number // 10)}'


print('Не оптимизированная функция recursive_reverse')

print(
    timeit(
        "recursive(num_x100)",
        globals=globals(),
        number=100000))
print(
    timeit(
        "recursive(num_x1000)",
        globals=globals(),
        number=100000))

print(
    timeit(
        "recursive(num_x10000)",
        globals=globals(),
        number=1))

print()


# С мемоизацией
def memoize(f):
    cache = {}

    def decorator(*args):
        if args in cache:
            # print(cache[args])
            return cache[args]
        else:

            cache[args] = f(*args)
            print(cache[args])
            return cache[args]

    return decorator


@memoize
def recursive_new(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_new(number // 10)}'


print('Оптимизированная функция recursive_new')

print(
    timeit(
        'recursive_new(num_x100)',
        globals=globals(),
        number=100000))

print(
    timeit(
        'recursive_new(num_x1000)',
        globals=globals(),
        number=100000))

print(
    timeit(
        'recursive_new(num_x10000)',
        globals=globals(),
        number=1))

# Мемоизация в данной задачи не нужна так-как ф-ция вызывается один раз, а если вызывать функцию много раз, то она
# понадобится!
