"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

"""

from collections import Counter, deque


class Hayffman:

    def __init__(self, *args):
        self.code_table = dict()
        self.decode_table = dict()
        self.encoded_string = ''
        self.my_str = ''
        try:
            if len(args) < 2:
                self.my_str = args[0]
            else:
                self.code_table = args[0]
                for key, val in self.code_table.items():
                    self.decode_table[val] = key
                self.encoded_string = args[1].split()
        except Exception:
            print('Исходные данные введены с ошибкой.')

    def make_tree(self):
        freq_of_char = Counter(self.my_str)
        sorted_elements = deque(sorted(freq_of_char.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:  # построение древа
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}
                for i, _count in enumerate(sorted_elements):  # место ставки элемента
                    if weight > _count[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    sorted_elements.append((comb, weight))
        else:
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))

        return sorted_elements[0][0]

    def hayffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.hayffman_code(tree[0], path=f'{path}0')
            self.hayffman_code(tree[1], path=f'{path}1')

    def table_code(self):
        self.code_table.clear()
        self.hayffman_code(self.make_tree())
        return self.code_table

    def str_encode(self):
        if len(self.code_table) == 0:  # создаем таблицу кодировки
            self.table_code()
        return ' '.join([(lambda x: self.code_table.get(x))(i) for i in self.my_str])

    def str_decode(self):
        if len(self.decode_table) == 0:  # создадим таблицу декодировки
            return 'Не передали таблицу кодировки.'
        else:
            self.my_str = ''.join([(lambda x: self.decode_table.get(x))(i) for i in self.encoded_string])
            return self.my_str


""" Проводим кодировку данных: """

print(f'{"-" * 20} Кодируем данные {"-" * 20}')
h = Hayffman("Мы поехали в путешествие по России")
print(f'Кодируемый текст: {h.my_str}')
print(f'Структура дерева: {h.make_tree()}')  # просмотр древа
print(f'Кодировочная таблица:  {h.table_code()}')  # просмотр кодировочной таблицы
print(f'Результат кодирования: {h.str_encode()}')

print(f'\n{"-" * 20} Декодируем данные {"-" * 20}')

""" Наоборот, проводим декодировку данных: """

table_code = {'с': '000', 'в': '0010', 'т': '0011', 'е': '010', 'и': '011', 'х': '10000',
              'а': '10001', 'М': '10010', ' ': '110', 'ы': '10011', 'ш': '10100', 'Р': '10101',
              'л': '10110', 'у': '10111', 'п': '1110', 'о': '1111'}
str_encode = '10010 10011 110 1110 1111 010 10000 10001 10110 011 110 0010 110 1110 10111 0011 010 10100 010 000 ' \
             '0011 0010 011 010 110 1110 1111 110 10101 1111 000 000 011 011'
nh = Hayffman(table_code, str_encode)
print(f'Результат декодирования: {nh.str_decode()}')
print(f'Структура дерева: {h.make_tree()}')
