"""
Задание 5.
Задание на закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


class Stack_of_plates:


    def __init__(self, max):
        self.element = []
        self.max = max

    def __str__(self):
        return str(self.element)

    def add_in_stack(self, plate):
        if len(self.element) == 0:
            self.element.append([plate])
        elif len(self.element[len(self.element) - 1]) < self.max:
            self.element[len(self.element) - 1].append(plate)
        else:
            self.element.append([])
            self.element[len(self.element) - 1].append(plate)

    def last_plates(self):
        return f"Номер последней помытой тарелки: {self.element[len(self.element) - 1][-1]}"

    def pop_plates(self):
        self.element[len(self.element) - 1].pop()
        if len(self.element[len(self.element) - 1]) == 0:
            self.element.pop()
        return print("Тарелка убрана в шкаф")

    def count_plates_stack(self):
        return f"Количество помытых стопок: {len(self.element)}"

    def last_plates_stack(self):
        return f"В новой стопке находится: {len(self.element[len(self.element) - 1])} тарелок"


how_much_plates = Stack_of_plates(10)

for i in range(1, 20):
    how_much_plates.add_in_stack(i)

print(how_much_plates)
print(how_much_plates.count_plates_stack())
how_much_plates.pop_plates()
print(how_much_plates.last_plates())
print(how_much_plates)