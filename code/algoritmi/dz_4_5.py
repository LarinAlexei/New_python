"""
Задание 5.**
Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).
Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (теорию по Решету нужно искать в сети)
Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.
Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.

"""

import timeit


# O(n**2)
def example_simple(i):
    count = 1
    k = 2
    while count <= i:
        w = 1
        is_simple = True
        while w <= k:
            if k % w == 0 and w != 1 and w != k:
                is_simple = False
                break
            w += 1
        if is_simple:
            if count == i:
                break
            count += 1
        k += 1
    return k


# O(n log(log n))
def example_not_simple(i):
    k = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while k < l:
        if sieve[k] != 0:
            m = k * 2
            while m < l:
                sieve[m] = 0
                m += k
        k += 1
    return [p for p in sieve if p != 0][i - 1]


i = int(input('Введите любое число: '))
print(timeit.timeit("example_simple(i)", globals=globals(), number=100))
print(timeit.timeit("example_not_simple(i)", globals=globals(), number=100))

# Алгоритм решета Эратосфена работает быстрее для поиска больших чисел.
