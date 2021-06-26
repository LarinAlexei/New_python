class ComplexNumbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = 'x + y'

    def __add__(self, other):
        print(f'Сумма result_1 и result_2 будет равна: ')
        return f'result = {self.x + other.x} + {self.y + other.y}'

    def __mul__(self, other):
        print('Произведение result_1 и result_2 будет равна: ')
        return f'result = {self.x * other.x - (self.y * other.y)} + {self.y * other.y}'

    def __str__(self):
        return f'result = {self.x} + {self.y}'


result_1 = ComplexNumbers(8, 5)
result_2 = ComplexNumbers(5, 2)
print(result_1)
print(result_1 + result_2)
print(result_1 * result_2)