from sys import argv
from datetime import date
from requests import get, utils

respons = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def rate(value):
    main = respons.split('<Valute ID=')
    d, m, y = main[0].split('"')[-4].split('.')

    for i in main:
        if value.upper() in i:
            print(date(year=int(y), month=int(m), day=int(d)), end=', ')
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', ''))
            # return findall(r'\d*\,\d*', i)[0].replace(',', '.')


if __name__ == '__main__':
    word = argv[1]
    #    print(rate(input('Введите название валюты курс которой хотите узнать,например USD: ')))
    # print(rate('EUR'))
    print(rate(word))
