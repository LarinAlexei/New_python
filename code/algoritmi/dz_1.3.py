"""

Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.

"""

inf_company = {
    'appel': 1800,
    'hiomi': 2100,
    'yandex': 3100,
    'rzd': 2400,
    'm.video': 2700,
    'mail': 2100
        }

# вариант №1 O(N^2)
def sorted_1(random_list):
    for i in range(len(random_list)):
        lowest_value_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[lowest_value_index][1]:
                lowest_value_index = j
        random_list[i], random_list[lowest_value_index] = random_list[lowest_value_index], random_list[i]
    return random_list[0:4]

list_from_dictionary = list(inf_company.items())
for i in sorted_1(list_from_dictionary):
    print(i[0], ':', i[1])

print('end!' * 1)

# вариант №2 O(N*logN)
list_from_dictionary = list(inf_company.items())
list_from_dictionary.sort(key = lambda  i: i[1], reverse=True)
for i in range(4):
    print(list_from_dictionary[i][0], ':', list_from_dictionary[i][1])

print('end!' * 1)

# вариант №3 O(N)
def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(4):
        maximum = max(list_d.items(), key = lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max

print(three_max(inf_company))