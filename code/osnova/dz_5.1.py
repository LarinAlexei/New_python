def my_list(val):
    for i in range(1, val + 1, 2):
        yield i


for n in my_list(15):
    print(n)
