import re

with open('jawiki-uk.txt', 'r') as f:
    lines = ''.join(f.readlines())

pattern = re.compile(r'\[\[Category:(.+?)(?:\|.*)?\]\]')
lst = re.findall(pattern, lines)

print(lst)