import os

f_name = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, name in f_name.items():
    if not os.path.exists(key):
        for item in name:
            for t in item.keys():
                os.makedirs(os.path.join(key, t))