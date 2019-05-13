import xml.etree.ElementTree as ET

with open('nlp.txt.xml', 'r') as f:
    lines = ''.join(f.readlines()) 
root = ET.fromstring(lines)

sentences = root[0][1]
for sentence in sentences:
    for token in sentence[0]:
        print('%s\t%s\t%s' % (token[0].text, token[1].text, token[4].text))