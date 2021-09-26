"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

"""

import random


def random_number(counter, numbers):
    print(f"Попытка №{counter}")
    value = int(input("Введите число от 0 до 100: "))
    if counter == 10 or value == numbers:
        if value == numbers:
            print("Поздравляю! Верно! ")
        print(f"Загаданное число было: {numbers}")
    else:
        if value < numbers:
            print(f"Загаданное число больше чем: {numbers}")
        else:
            print(f"Загаданное число меньше чем: {numbers}")
        random_number(counter + 1, numbers)


random_number(1, random.randint(0, 100))