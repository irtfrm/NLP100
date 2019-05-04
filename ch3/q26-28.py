import re
import json

with open('jawiki-uk.txt', 'r') as f:
    lines = ''.join(f.readlines())

pat1 = re.compile(r'{{基礎情報.*?\n(.*?\n)}}', re.DOTALL)
lst = re.findall(pat1, lines)
pat2 = re.compile(r'\|(.+?) = (.+?)(?:(?=\n\|)|(?=\n$))', re.DOTALL)
res = re.findall(pat2, lst[0])

dct = {}
sub =[
    [r'(\'{2,5})(.+?)\1', r'\2'], #q26
    [r'\[\[(?:.+?\|)??([^ \|]+?)\]\]', r'\1'], #q27
    [r'<br\s*?/>\n?', r''],
    [r'<ref(.*?)>\[?(.*?)\]?</ref>', r''],
    [r'\**{{lang\|[a-z]+\|(.*?)}}',r'\1'],
    [r'<ref.*?/>', r''],
    [r'&pound;', r'£']
]

for r in res:
    l = r[1]
    for x, y in sub:
        l = re.sub(x, y, l)
    dct[r[0]] = l

with open('q28.json','w') as out:
    json.dump(dct, out)