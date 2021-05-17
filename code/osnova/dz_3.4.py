def theasurus_adv(*names):
    names_surname = {}
    for name in sorted(names):
        n, s = name.split()
        val = names_surname.setdefault(s[0], {n[0]: [name]})
        n_val = val.setdefault(n[0], [name])
        if name not in n_val:
            n_val.append(name)
    return names_surname


print(theasurus_adv('Денис Грозный', 'Дениска Грозунов', 'Иван Барабан', 'Игорь Крутой', 'Сергей Сергеев'))
