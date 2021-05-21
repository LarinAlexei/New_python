faulty_action = ['в', '11', 'часов', '24', 'минут(ы)', 'температура', 'воздуха', 'была', '+19', 'градусов']
good_action = []

for i in faulty_action:
    if i.replace('+', '').replace('-', '').isdigit():
        if i.isdigit():
            good_action.append(f"'{int(i):02}'")
        else:
            good_action.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        good_action.append(i)

print(good_action)
print(" ".join(good_action))