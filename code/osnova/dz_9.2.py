class TravelingExpenses:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calculate_profit(self, weight=25, thickness=5):
        return f'{self._lenght} м * {self._width} м * {weight} кг * {thickness} см =' \
               f'{(self._lenght * self._width * weight * thickness) / 1000} т'


road_1 = TravelingExpenses(4000, 30)
print(road_1.calculate_profit())
