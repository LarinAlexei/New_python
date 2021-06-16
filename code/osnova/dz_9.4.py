class Car:

    def __init__(self, name, color, speed, police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.police = police
        print(f'Новая машина: {self.name} (цвет {self.color}) машина полиции - {self.police}')

    def gooo(self):
        print(f'{self.name}: машина поехала.')

    def stop(self):
        print(f'{self.name}: машина остановилась.')

    def turn(self):
        print(f'{self.name}: машина повернула {"налево" if direction == 0 else "направо"}.')

    def speed_show(self):
        return f'{self.name}: скорость автомобиля: {self.speed}. Превышение скорости.' \
            if self.speed > 60 else f'{self.name}: Скорость автомобиля {self.speed}'


class TownCar(Car):

    def speed_show(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости.' \
            if self.speed > 60 else f'{self.name}: Скорость автомобиля {self.speed}'


class Truck(Car):

    def speed_show(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости.' \
            if self.speed > 40 else f'{self.name}: Скорость автомобиля {self.speed}'


class SportCar(Car):
    """Спортивная"""


class PoliceCar(Car):

    def __init__(self, name, color, speed, police=True):
        super().__init__(name, color, speed, police)


police_car = PoliceCar('"Полицейская"', 'белый', 90)
police_car.gooo()
print(police_car.speed_show())
police_car.turn(0)
police_car.stop()

print()
truck_car = Truck('"Грузовик"', 'синий', 40)
truck_car.gooo()
truck_car.turn(1)
print(truck_car.speed_show())
truck_car.turn(0)
truck_car.stop()

print()
sport_car = SportCar('"Спортивная"', 'желтая', 140)
sport_car.gooo()
sport_car.turn(0)
print(sport_car.speed_show())
sport_car.stop()

print()
city_car = TownCar('"городское авто"', 'серая', 45)
city_car.gooo()
city_car.turn(1)
city_car.turn(0)
print(city_car.speed_show())
city_car.stop()

print(f'\nМашина {city_car.name} (цвет {city_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')
