import re

with open('jawiki-uk.txt', 'r') as f:
    lines = [ line.strip('\n') for line in f.readlines()]

pattern = re.compile(r'\[\[Category:.+\]\]')

for line in lines:
    if re.match(pattern, line) != None:
        print(line)