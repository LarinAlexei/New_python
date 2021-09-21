"""

Задание 7.
Задание на закрепление навыков работы с деком
В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'
Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
Примечание:
Вам не нужно писать код с нуля. Вам нужно доработать пример с урока.

"""

class DequeClass:
    def __init__(self):
        self.element = []

    def is_empty(self):
        return self.element == []

    def add_to_front(self, element):
        self.element.append(element)

    def add_to_rear(self, elem):
        self.element.insert(0, elem)

    def remove_from_front(self):
        return self.element.pop()

    def remove_from_rear(self):
        return self.element.pop(0)

    def size(self):
        return len(self.element)


def examination(string):
    objectStr = DequeClass()
    string = string.replace(' ', '').lower()



    for i in string:
        objectStr.add_to_rear(i)

    result = True

    while objectStr.size() > 1 and result:
        front = objectStr.remove_from_front()
        rear = objectStr.remove_from_rear()
        if front != rear:
            result = False

    return result


print(examination("Молоко делили ледоколОм"))
print(examination("молоё1ко делилИ лед6околом"))
print(examination("Один НиДо"))
print(examination("Два авД"))
print(examination("РокотТокор"))
print(examination("Топот"))