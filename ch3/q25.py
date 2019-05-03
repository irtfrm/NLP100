import re

with open('jawiki-uk.txt', 'r') as f:
    lines = ''.join(f.readlines())

pattern = re.compile(r'{{基礎情報.*?\n(.*?\n)}}', re.DOTALL)
lst = re.findall(pattern, lines)
print(lst)
pat2 = re.compile(r'\|(.+?) = (.+?)(?:(?=\n\|)|(?=\n$))', re.DOTALL)
res = re.findall(pat2, lst[0])

dct = {r[0] : r[1] for r in res}

print(dct)