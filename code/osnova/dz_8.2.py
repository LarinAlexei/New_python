import re

view = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')

with open('log.txt', encoding='utf-8') as r:
    for line in r:
        print(re.findall(view, line))
#        break
