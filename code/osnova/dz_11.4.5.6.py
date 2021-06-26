class Warehouse:

    def __init__(self, name, quantity, number_of_equipment):
        self.name = name
        self.quantity = quantity
        self.n_o_e = number_of_equipment
        self.my_full = []
        self.my_store = []
        self.info = {'Информация об устройстве': self.name, 'Количество на складе': self.quantity}

    def __str__(self):
        return f'модель {self.name} количество {self.quantity}'

    def accounting(self):
        while True:
            try:
                model = input('Введите наименование модели: ')
                quant = int(input('Количество техники: '))
                model_info = {'Модель': model, 'Количество': quant}
                self.info.update(model_info)
                self.my_store.append(self.info)
                print(f'Текущий список: \n{self.my_store}')
            except:
                print('Некоректный ввод данных!')
                q_y = input('Для окончания работы "Q"! \nДля продолжения "Y": ')
                if q_y == 'Y' or q_y == 'y':
                    self.my_full.append(self.my_store)
#                    print(f'Что есть на складе: {self.my_full}')
                elif q_y == 'Q' or q_y == 'q':
                    print(f'Что есть на складе: {self.my_full}')
                    return 'Вы вышли!'
                else:
                    return Warehouse.accounting(self)


class Printer(Warehouse):
    def my_printer(self):
        return f'to printer {self.n_o_e} times'


class Copier(Warehouse):
    def my_copier(self):
        return f'to copier {self.n_o_e} times'


class Scanner(Warehouse):
    def my_scanner(self):
        return f'to scanner {self.n_o_e} times'


printer = Printer('HP', 3, 1)
copier = Copier('XEROX', 4, 2)
scanner = Scanner('Brother', 7, 3)
print(printer.accounting())
print(copier.accounting())
print(scanner.accounting())
print(printer.my_printer())
print(copier.my_copier())
print(scanner.my_scanner())
