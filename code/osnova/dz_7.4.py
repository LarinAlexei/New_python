import os
import django
from collections import defaultdict

def info():
    root_dir = django.__path__[0]
    django_files = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            weight = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            django_files[weight] += 1

    for weight, nums in sorted(django_files.items()):
        print(f'{weight}: {nums}')
