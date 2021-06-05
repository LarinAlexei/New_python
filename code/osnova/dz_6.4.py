from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        all_value = zip_longest(users, hobby, fillvalue=None)

        with open('hobby_users.txt', 'w', encoding='utf-8') as n:
            for i in all_value:
                print(f'{str(i[0]).strip()}: {i[1].strip()}', file=n)
