"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?

"""

from timeit import timeit
from collections import OrderedDict
from random import randint

""" С dict() """


def dict_add_val():
    simple[next(key_range)] = next(val_range)


# сделаем простой проход по всем ключам и получим значения в переменную
def dict_show_items():
    for key, val in simple.items():
        res = [key, val]


# находим по значению ключа
def dict_find():
    val = simple.get(randint(1, n))


def dict_pop():
    simple.pop(next(pop_range))


""" С OrderedDict() """


def od_add_val():
    order_dict[next(key_range)] = next(val_range)


# сделаем простой проход по всем ключам и получим значения в переменную
def od_show_items():
    for key, val in order_dict.items():
        res = [key, val]


# получаем значени по ключу
def od_find():
    val = order_dict.get(randint(1, n))


def od_pop():
    order_dict.pop(next(pop_range))


# Общие параметры модели:
n = 1000
simple = {}
order_dict = OrderedDict()

""" Замеры для dict() """
# Генераторы для добавления данных в словарь
key_range = (i for i in range(n))
pop_range = (i for i in range(n))
val_range = ((randint(1, 100), randint(1, 100)) for i in range(n))

func = ['dict_add_val', 'dict_show_items', 'dict_find', 'dict_pop']
res_dict_time = []
for func_name in func:
    res_dict_time.append(timeit(f'{func_name}()', setup=f'from __main__ import {func_name}', number=n))

""" Замеры для OrderedDict """
# Генераторы для добавления данных в словарь (восстанавливаем после истощения)
key_range = (i for i in range(n))
pop_range = (i for i in range(n))
val_range = ((randint(1, 100), randint(1, 100)) for i in range(n))

func = ['od_add_val', 'od_show_items', 'od_find', 'od_pop']
res_od_time = []
for func_name in func:
    res_od_time.append(timeit(f'{func_name}()', setup=f'from __main__ import {func_name}', number=n))

# Результаты:
operations = ['add_val', 'show_items', 'find_val', 'pop']
all_result = []
all_result = list(zip(operations, res_dict_time, res_od_time))
print(f'Количество повторов: ', n)
print('Операция                 Dict       ODict      Win   D/Od % ')
for i in all_result:
    print(f'{i[0]:15.15}\t{round(i[1], 6):15.15}\t{round(i[2], 6):10.10}\t'
          f'\t{"D" if i[1] < i[2] else "OD"}\t{round((i[1] / i[2] - 1) * 100, 3)}')

""" 
Выводы:
Замеры показали, что обычный словарь не имеет никаких отличий по скорости по сравнению с OrderedDict.
Но OrderedDict имеет дополнительные методы, которых нет в обычном словаре:
. move_to_end()- это новый метод позволяет переместить существующий элемент в конец или в начало словаря.
. popitem()- это более расширенный dict.popitem() который позволяет вам удалять и 
возвращать элемент либо из конца, либо из начала упорядоченного словаря.

Результаты:
Количество повторов:  1000
Операция                 Dict       ODict      Win   D/Od % 
add_val        	       0.001469	  0.001533		D	-4.167
show_items     	       0.047967	  0.067406		D	-28.839
find_val       	       0.000698	  0.000688		OD	1.425
pop            	       0.000289	  0.000342		D	-15.591
Количество повторов:  10000
Операция                 Dict       ODict      Win   D/Od % 
add_val        	        0.01384	  0.014356		D	-3.596
show_items     	       4.049128	  6.354855		D	-36.283
find_val       	       0.007526	  0.007388		OD	1.88
pop            	       0.002166	  0.003461		D	-37.415
Количество повторов:  20000
Операция                 Dict       ODict      Win   D/Od % 
add_val        	       0.028157	  0.027524		OD	2.299
show_items     	      15.843597	 25.492666		D	-37.85
find_val       	       0.014741	  0.014533		OD	1.431
pop            	       0.004241	  0.006154		D	-31.088

"""
