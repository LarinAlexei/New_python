class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date(cls, num):
        d, m, y = num
        return cls(d, m, y)

    @staticmethod
    def dates(obj):
        #        if 1 <= obj <= 12:
        return f'{obj.day}-{obj.month}-{obj.year}'


my_list = ('11', '11', '2021')
one = Data.date(my_list)
print(Data.dates(one))
print(type(Data.dates(one)))
