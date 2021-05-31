from itertools import islice, zip_longest

schoolboy = ['Алексей', 'Сергей', 'Елизавета', 'Дмитрий', 'Андрей', 'Артем', 'Анастасия', 'Александр']
klasses = ['9А', '8Б', '7Г', '11В', '10Б', '9Б']

new = (n for n in zip_longest(schoolboy, klasses) if len(schoolboy) > len(klasses))

print(type(new))
print(*islice(new, 9))
print(list(islice(new, 3)))
