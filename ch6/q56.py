import xml.etree.ElementTree as ET

symbols = [',', '.', ':', ';', '!', '?', "'", "''", '`', '``']

with open('q56.xml', 'r') as f:
    lines = ''.join(f.readlines()) 
root = ET.fromstring(lines)

lst = []
coreference = root[0][2]
for cor in coreference:
    for i, mention in enumerate(cor):
        if 'representative' in mention.attrib:
            rep_text = mention[4].text
        elif rep_text != mention[4].text:
            lst.append({
                'sentence': int(mention[0].text)-1,
                'start': int(mention[1].text)-1,
                'end': int(mention[2].text)-1,
                'rep_text': rep_text,
                'text': mention[4].text
            })

lst.sort(key=lambda x:x['sentence']*10000+x['start'])

mnt = [l for l in lst]
for i in range(len(lst)):
    if i == len(lst)-1: continue
    j = 1
    while i + j < len(lst):
        if lst[i+j]['sentence'] != lst[i]['sentence']: break
        if lst[i]['end'] >= lst[i+j]['end'] and lst[i+j] in mnt:
            mnt.remove(lst[i+j])
        j += 1


k = 0
sentences = root[0][1]
for i, sentence in enumerate(sentences):
    line = ''
    for j, token in enumerate(sentence[0]):
        if j != 0 and not token[0].text in symbols:
            line += ' '
        if i == mnt[k]['sentence']:
            if j == mnt[k]['start']:
                line += '%s (%s)' % (mnt[k]['rep_text'], mnt[k]['text'])
            elif j >= mnt[k]['end']:
                if k < len(mnt)-1 and j == mnt[k]['end']: k += 1
                line += token[0].text
            elif j > mnt[k]['start']:
                if line[len(line)-1] == ' ':
                     line = line[:-1]
            else:
                line += token[0].text
        else:
            line += token[0].text
    print(line)