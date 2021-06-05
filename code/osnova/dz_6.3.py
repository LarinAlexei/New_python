from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if (users.seek(0)) >= (hobby.seek(0)):
            with open('o_O.json', 'w', encoding='utf-8') as n:
                all_value = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)
                my_dict = {str(av[0]).strip(): (av[1].strip()) for av in all_value}

                dump(my_dict, n, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(1)