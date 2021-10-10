"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2

"""

import collections

while True:
    try:
        f = int(input('Введите количество компаний: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = collections.defaultdict()
my_solution = collections.deque()
my_solution_1 = collections.deque()
all_profit = 0
quarter = 4

for i in range(f):
    name_company = input(f'\nВведите название {i + 1}й компании: ')
    average_income = 0
    quarter_numbers = 1
    while quarter_numbers <= quarter:
        try:
            average_income += float(input(f'Введите прибыль за {quarter_numbers}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        quarter_numbers += 1
    companies[name_company] = average_income
    all_profit += average_income

mid_profit = all_profit / f
for i, item in companies.items():
    if item >= mid_profit:
        my_solution.append(i)
    else:
        my_solution_1.append(i)
print(f'Средняя прибыль для всех компаний составила: {mid_profit}')
print(f'Прибыль выше среднего у {len(my_solution)} компаний:')
for name in my_solution:
    print(name)
print(f'Прибыль ниже среднего у {len(my_solution_1)} компаний:')
for name in my_solution_1:
    print(name)
