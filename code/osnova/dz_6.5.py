from sys import argv
from itertools import zip_longest

us, h, out_n = argv[3:]

with open(us, 'r', encoding='utf-8') as users:
    with open(h, 'r', encoding='utf-8') as hobby:
        all_value = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)

        with open(out_n, 'w', encoding='utf-8') as n:
            for i in all_value:
                print(f'{str(i[0]).strip()}: {i[1].strip()}', file=n)