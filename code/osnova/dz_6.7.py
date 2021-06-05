from sys import argv

with open('bakery.csv', 'r+', encoding='utf-8') as n:
    ba, ta = argv[1:]
    ta = round(float(ta.replace(',', '.')), 3)
    for line in range(int(ba)):
        f = n.tell()
        r = n.readline().strip()
        if r == '':
            exit('такой позиции нет')

    if ',' in str(ta) or '.' in str(ta):
        if ta <= 99999.999:
            n.seek(f)
            n.write(f'{ta:>010}')
        else:
            print('Number must be less than 99 999,999')