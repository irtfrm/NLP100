import xml.etree.ElementTree as ET

with open('nlp.txt.xml', 'r') as f:
    lines = ''.join(f.readlines()) 
root = ET.fromstring(lines)

sentences = root[0][1]
for sentence in sentences:
    for i, token in enumerate(sentence[0]):
        if i > 0:
            if sentence[0][i-1][5].text == 'PERSON': continue
        if token[5].text == 'PERSON':
            ans = token[0].text
            nxt = sentence[0][i+1]
            if nxt[5].text == 'PERSON':
                ans += ' ' + nxt[0].text
            print(ans)