"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.

"""

from timeit import timeit
from collections import deque
from random import randint

test_data = [1, 2, 3]
numbers_test = 1000
simple_list = test_data.copy()
range = list(range(randint(1, 100)))
deque_test = deque(test_data)

""" Кол-во повторов для timeit """
n = 15000

""" Со списком """


def list_insert():
    simple_list.insert(0, numbers_test)


def list_pop_left():
    simple_list.pop(0)


def list_extend_left():
    nl = []
    nl.extend(range)
    nl.extend(simple_list)
    simple_list.clear()
    simple_list.extend(nl)


def list_append():
    simple_list.append(numbers_test)


def list_pop_right():
    simple_list.pop()


def list_extend_right():
    simple_list.extend(range)


""" С deque """


def deque_insert():
    deque_test.appendleft(numbers_test)


def deque_pop_left():
    deque_test.popleft()


def deque_extend_left():
    deque_test.extendleft(range)


def deque_append():
    deque_test.append(numbers_test)


def deque_pop_right():
    deque_test.pop()


def deque_extend_right():
    deque_test.extend(range)


""" Для списков """
func_list = ['list_insert', 'list_pop_left', 'list_extend_left', 'list_append', 'list_pop_right', 'list_extend_right']
res_list_time = []
for func_name in func_list:
    res_list_time.append(timeit(f'{func_name}()', setup=f'from __main__ import {func_name}', number=n))

""" Для deque """
func_deque = ['deque_insert', 'deque_pop_left', 'deque_extend_left', 'deque_append', 'deque_pop_right',
              'deque_extend_right']
res_deque_time = []
for func_name in func_deque:
    res_deque_time.append(timeit(f'{func_name}()', setup=f'from __main__ import {func_name}', number=n))

""" Выводим результат """
operations = ['append_left', 'pop_left', 'extend_left', 'append', 'pop_right', 'extend_right']
all_result = []
all_result = list(zip(operations, res_deque_time, res_list_time))
print(f'Количество повторов: ', n)
print('Операция                 Deque       List      Win   D/L % ')
for i in all_result:
    print(f'{i[0]:15.15}\t{round(i[1], 6):15.15}\t{round(i[2], 6):10.10}\t'
          f'\t{"d" if i[1] < i[2] else "L"}\t{round((i[1] / i[2] - 1) * 100, 3)}')

""" 
Следовательно:
Если требуется случайный доступ к элементу, то обычный список быстрее,
подтверждаем результатом выполненных замеров.
Использование Deque более эффективен на задачах, которые предполагают добавление / извлечение данных
с начала списка (с левой стороны). Если массивы данных большие, то лучше использовать (Deque). 
А если добавлять в конец, то deque может проигрывать спискам.
Результаты замеров:
Количество повторов:  1 000
Операция                 Deque       List      Win   D/L % 
append_left    	        9.9e-05	  0.000247		d	-59.968
pop_left       	        6.8e-05	  0.000142		d	-51.731
extend_left    	        0.00084	  0.204292		d	-99.589
append         	        8.6e-05	     9e-05		d	-4.0
pop_right      	          7e-05	   7.1e-05		d	-1.128
extend_right   	       0.000505	  0.001017		d	-50.324
Количество повторов:  1 000
Операция                 Deque       List      Win   D/L % 
append_left    	        9.1e-05	  0.000264		d	-65.492
pop_left       	        6.9e-05	  0.000145		d	-52.559
extend_left    	       0.000601	  0.103143		d	-99.417
append         	        7.7e-05	  0.000317		d	-75.781
pop_right      	          7e-05	     8e-05		d	-12.547
extend_right   	       0.000517	  0.001353		d	-61.789
Количество повторов:  1 000
Операция                 Deque       List      Win   D/L % 
append_left    	        9.3e-05	  0.000276		d	-66.256
pop_left       	        6.8e-05	   0.00014		d	-51.601
extend_left    	       0.000815	  0.164982		d	-99.506
append         	        8.2e-05	  0.000244		d	-66.394
pop_right      	        7.8e-05	   6.9e-05		L	12.645
extend_right   	       0.000757	  0.001171		d	-35.329
Количество повторов:  1 000
Операция                 Deque       List      Win   D/L % 
append_left    	        9.1e-05	  0.000247		d	-63.39
pop_left       	        6.7e-05	   0.00014		d	-52.211
extend_left    	       0.000426	  0.128346		d	-99.668
append         	        7.5e-05	     9e-05		d	-16.685
pop_right      	          7e-05	   7.2e-05		d	-3.064
extend_right   	       0.000381	  0.000499		d	-23.643
Количество повторов:  10 000
Операция                 Deque       List      Win   D/L % 
append_left    	       0.000802	  0.019333		d	-95.854
pop_left       	       0.000964	  0.006362		d	-84.856
extend_left    	       0.003347	   6.98957		d	-99.952
append         	       0.000747	  0.001403		d	-46.75
pop_right      	        0.00067	   0.00073		d	-8.298
extend_right   	       0.003274	   0.00475		d	-31.074
Количество повторов:  20000
Операция                 Deque       List      Win   D/L % 
append_left    	       0.001154	  0.042766		d	-97.301
pop_left       	       0.000991	  0.013158		d	-92.466
extend_left    	       0.003983	 11.523298		d	-99.965
append         	       0.001069	   0.00175		d	-38.893
pop_right      	       0.000969	  0.001025		d	-5.446
extend_right   	       0.003876	  0.005239		d	-26.009

"""
