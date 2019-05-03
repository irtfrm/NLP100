import re

with open('jawiki-uk.txt', 'r') as f:
    lines = ''.join(f.readlines())

pattern = re.compile(r'(==+)\s*(.*?)\s*\1')
lst = re.findall(pattern, lines)

for l in lst:
    print(l[1], len(l[0])-1)