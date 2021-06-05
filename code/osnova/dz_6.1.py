with open('pars_logs.txt', 'w', encoding='utf-8') as n:
    with open('log.txt', 'r', encoding='utf-8') as t:
        content = (f'{line.split()[0]}{line.split()[5][1:]}{line.split()[6]}' for line in t)
        for i in content:
            print(i, file=n)

