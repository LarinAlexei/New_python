"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

"""


def codes_and_symbols(value=32):
    if value == 128:
        return True
    print(f"{value} - {chr(value)}", end=' ')
    if (value - 31) % 10 == 0:
        print("\n")

    codes_and_symbols(value + 1)


codes_and_symbols()