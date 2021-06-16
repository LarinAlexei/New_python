class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def full_name(self):
        return f'{self.name} {self.surname}'

    def full_profit(self):
        return f'{sum(self._income.values())}'


count = Position('Larin', 'Aleksei', 'CEO', 900000, 455000)
print(count.full_name())
print(count.position)
print(count.full_profit())