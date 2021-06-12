from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num = [r for r in (*args, *kwargs.values())]
        t = [f'{func.__name__}({r}: {type(r)})' for r in num]
        print(*t, *func(*args, **kwargs), sep=',\n')

    return wrapper


@logger
def cube(*p, **g):
    num = [r for r in (*p, *g.values()) if isinstance(r, int) or isinstance(r, float)]
    return [i ** 3 for i in num]


h = cube(8, {'number': 3}, {11, 8}, {15, 7, 3, 2}, 'str')
h = cube(4, 12, 4.4, 20, g=77, j=33)
print(cube.__name__)
