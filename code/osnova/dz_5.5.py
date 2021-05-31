number = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([i for i in number if number.count(i) == 1])

"""

оптимизация

"""

my_number = {i: 0 for i in number}

for i in number:
    my_number[i] += 1

print([i for i in my_number if my_number[i] == 1])
