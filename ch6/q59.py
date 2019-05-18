import xml.etree.ElementTree as ET
import re

with open('nlp.txt.xml', 'r') as f:
    lines = ''.join(f.readlines()) 
root = ET.fromstring(lines)


for p in root.findall('./document/sentences/sentence/parse'):
  ptext = p.text
  matches = re.finditer(r'\(NP\s', ptext)
  for match in matches:
    rb = 0
    for index, c in enumerate(ptext[match.start():]):
      if c == ')':
        rb -= 1
      elif c == '(':
        rb += 1
      if rb == 0:
        ptext2 = ptext[match.start():match.start()+index+1]
        words = re.findall(r'([a-zA-Z\-]+)\)', ptext2)
        print(' '.join(words))
        break