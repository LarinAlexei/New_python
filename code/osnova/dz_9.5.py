class Stationery:
    def __init__(self, title='Something that can draw'):
        self.title = title

    def draw(self):
        print(f'Just start drawing {self.title}))')


class Pen(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} pen')


class Crayon(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} crayon')


class Brush(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} brush')


product = Stationery()
product.draw()
pen = Pen('Bic')
pen.draw()
crayon = Crayon('KanzOboz')
crayon.draw()
brush = Brush('Winsor & Newton')
brush.draw()
