from os import path, walk, listdir
import shutil

name_project = 'my_project'

try:
    for root, dirs, files in walk(name_project):
        if 'templates' in dirs and root != name_project:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(name_project, 'templates', path.basename(root)))
except FileNotFoundError:
    print('Already worked with these templates!')
