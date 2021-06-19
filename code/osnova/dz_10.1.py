class Matrix:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return '\n'.join('\t'.join([f'{itm:03}' for itm in line]) for line in self.num)

    def __add__(self, other):
        try:
            h = [[int(self.num[line][itm]) + int(other.num[line][itm]) for itm in range(len(self.num[line]))]
                 for line in range(len(self.num))]
            return Matrix(h)
        except IndexError:
            return f'Ошибка размерностей матриц'


h_1 = [[2, 6, 18], [3, 6, 9], [-4, 32, -6]]
h_2 = [['7', '9', '44'], ['5', '15', '-53'], ['14', '3', '11']]

mr_1 = Matrix(h_1)
mr_2 = Matrix(h_2)
h_new = mr_1 + mr_2

stroki = int(input('Введите количество строк и столбцов матрицы: '))
stolbci = stroki

matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbci)])
matrix2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbci)])

print('First matrix:\n', matrix1, end='\n\n')
print('Second matrix:\n', matrix2, end='\n\n')
print('Simm of first and second matrix:\n', matrix1 + matrix2)
