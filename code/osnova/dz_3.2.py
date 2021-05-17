num_translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def numes(num):
    if num.istitle():
        return str(num_translate.get(num.lower())).title()
    return num_translate.get(num)


print(numes(input('Enter a number from 0 to 10: ')))
