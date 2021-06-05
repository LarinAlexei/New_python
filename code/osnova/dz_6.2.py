import collections

with open('pars_logs.txt', 'r', encoding='utf-8') as n:
    my_dict = collections.Counter()

    for i in n:
        i = i.split()[0]
        my_dict[i] += 1

    ip, count = my_dict.most_common(1)[0][0], my_dict.most_common(1)[0][1]
    print(f'Spammer {ip} - {count} times')
    # Spammer 5.63.157.73 - 34 times
