from abc import ABC, abstractmethod


class Cap(ABC):
    result = 0

    def __init__(self, argum):
        self.argum = argum

    @property
    @abstractmethod
    def expens(self):
        pass

    def __add__(self, other):
        Cap.result += self.expens + other.expens
        return Costume(0)

    def __str__(self):
        rest = Cap.result
        Cap.result = 0
        return f'{rest}'


class Coap(Cap):
    @property
    def expens(self):
        return round(self.argum / 6.5) + 0.5


class Costume(Cap):
    @property
    def expens(self):
        return round((2 * self.argum + 0.3) / 100)


coap = Coap(64)
costume = Costume(130)
print(coap + costume + coap)
