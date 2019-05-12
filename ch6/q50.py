import re

with open('nlp.txt', 'r') as f:
    lines = f.readlines()

ans = []

for line in lines:
    l = re.findall(r'(.+?[.;:!?])(?:(?:\s+?(?=[A-Z]))|$)', line)
    ans.extend(l)

for line in ans:
    print(line)