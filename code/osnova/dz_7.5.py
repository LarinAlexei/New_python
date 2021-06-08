import os
import json
import django

def info():
    root_dir = django.__path__[0]
    django_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            weight = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if weight in django_files:
                django_files[weight][0] += 1
                if ext not in django_files[weight][1]:
                    django_files[weight][1].append(ext)
            else:
                django_files[weight] = [1, [ext]]
    result = {}
    for weight, list in sorted(django_files.items()):
        result[weight] = tuple(list)
        print(f'{weight}: {tuple(list)}')

    folder = os.path.basename(os.getcwd()) + '_summary.json'
    with open(folder, 'w', encoding='utf-8') as u:
        json.dump(result, u, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    info()