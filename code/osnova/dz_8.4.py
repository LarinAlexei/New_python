def val_checker(c_func):
    def val_checker_(func):
        def wrapper(nums):
            if c_func(nums):
                print(func(nums))
            else:
                raise ValueError(f'wrong val {nums}')

        return wrapper

    return val_checker_


@val_checker(lambda v: v > 0)
def cube(v):
    return v ** 3


try:
    n = cube(8)
except ValueError as err:
    print(err)
