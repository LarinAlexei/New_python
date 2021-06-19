class Cell:
    def __init__(self, nums):
        self.nums = nums

    def order(self, row):
        return '\n'.join(['*' * row for i in range(self.nums // row)]) + '\n' + '*' * (self.nums % row)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Sum of cell is:')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Subtraction of cell is:')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше второй, вычитание невозможео'

    def __mul__(self, other):
        print('Multiply of cell is:')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Truediv of cell is:')
        return Cell(self.nums // other.nums)


c_1 = Cell(15)
c_2 = Cell(24)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 // c_2)
print(c_2.order(7))