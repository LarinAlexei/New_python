# 3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем
# «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.

for procent in range(32):
    if procent % 10 == 1 and procent % 100 != 11:
        print(procent, 'процент,', end=' ')
    elif 1 < procent % 10 < 5 and not 11 < procent % 100 < 15:
        print(procent, 'процента,', end=' ')
    else:
        print(procent, 'процентов,', end=' ')