class MyOwnErr:
    def __init__(self, num):
        self.num = num


def divide(num, divider):
    try:
        return num / divider
    except:
        return f"Деление на ноль недопустимо"


divi = MyOwnErr(537)
print(divide(537, 0))
