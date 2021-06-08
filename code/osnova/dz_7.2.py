import yaml
import os

with open('config.yaml') as u:
    get = yaml.safe_load(u)


def create_path(number, prefix=''):
    for directory, paths in number.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create_path(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    create_path(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, u'{i}'), 'w') as _:
                        pass

create_path(get)