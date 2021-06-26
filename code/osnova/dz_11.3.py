class MyError:
    def __init__(self):
        self.my_number = []

    def my_value(self):

        while True:
            try:
                val = int(input('Введите значение: '))
                self.my_number.append(val)
                print(f'Текущий список: {self.my_number} \n')
            except:
                print('Вы ввели недопустимые значения: Строка или Булево')
                yes_out = input('Хотите попробовать еще раз нажмите "Y"! \nЕсли хотите выйти то "O": ')

                if yes_out == 'Y' or yes_out == 'y':
                    print(try_except.my_value())
                elif yes_out == 'O' or yes_out == 'o':
                    return 'Вы вышли!'
                else:
                    return 'Вы вышли!'


try_except = MyError()
print(try_except.my_value())
