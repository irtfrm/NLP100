import re

with open('jawiki-uk.txt', 'r') as f:
    lines = ''.join(f.readlines())

pattern = re.compile(r'\[\[(?:File|ファイル):(.+?)\|')
lst = re.findall(pattern, lines)

for l in lst:
    print(l)