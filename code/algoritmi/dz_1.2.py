"""

Задание 2.
Реализуйте два алгоритма.
Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.
Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.

"""

from random import randint

# c O(n^2)
def list_min_n2(lst):
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            return i

# c O(n)
def list_min_n(lst):
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value

lst1 = [randint(0, 100) for i in range(13)]
print(lst1)
print(list_min_n2(lst1))
