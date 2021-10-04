"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым

"""

from timeit import timeit
import cProfile


# Рекурсия
def example(initial_num, example_num=0):
    if initial_num == 0:
        return example_num
    else:
        num = initial_num % 10
        example_num = (example_num + num / 10) * 10
        initial_num //= 10
        return example(initial_num, example_num)


# Цикл
def example_2(initial_num, example_num=0):
    while initial_num != 0:
        num = initial_num % 10
        example_num = (example_num + num / 10) * 10
        initial_num //= 10
    return example_num


# Срез
def example_3(initial_num):
    initial_num = str(initial_num)
    example_num = initial_num[::-1]
    return example_num


initial_num = int(input('Введите целое число: '))

example(initial_num, example_num=0)
example_2(initial_num, example_num=0)
example_3(initial_num)

print(
    'Число наоборот на рекурсиях: ',
    timeit(
        f'example({initial_num})',
        globals=globals(),
        number=10000))
print(
    'Число наоборот на циклах: ',
    timeit(
        f'example_2({initial_num})',
        globals=globals(),
        number=10000))
print(
    'Число наоборот на срезах: ',
    timeit(
        f'example_3({initial_num})',
        globals=globals(),
        number=10000))

cProfile.run('example(10000000000)')
cProfile.run('example_2(10000000000)')
cProfile.run('example_3(10000000000)')

"""
По полученым данным видно что "срез" быстрее всего справился с задачей.
Срез не имеет арифмитических действий, в отличии от цикла и рекурсии, поэтому срез выполняется быстрее.

"""
