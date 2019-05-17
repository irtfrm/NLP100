import xml.etree.ElementTree as ET


with open('nlp.txt.xml', 'r') as f:
    lines = ''.join(f.readlines()) 
root = ET.fromstring(lines)

nlp_core = []

for sentence in root.findall('./document/sentences/sentence'):
  dct = {'tokens' : [], 'deps' : []}
  for token in sentence[0]:
    dct['tokens'].append({
      'id' : int(token.attrib['id']),
      'word' : token[0].text,
      'dependents' : []
    })

  for dep in sentence[2]:
    dct['tokens'][int(dep[0].attrib['idx'])-1]['dependents'].append({
      'relation' : dep.attrib['type'],
      'governor' : int(dep[0].attrib['idx']),
      'dependent' : int(dep[1].attrib['idx']),
    })
  nlp_core.append(dct)


for dct in nlp_core:
  for token in dct['tokens']:
    bl = False
    for dep in token['dependents']:
      if dep['relation'] == 'nsubj':
        bl = True
        print(dct['tokens'][dep['dependent']-1]['word'], token['word'], end="")
      elif dep['relation'] == 'dobj' and bl:
        print(' ' + dct['tokens'][dep['dependent']-1]['word'], end="")
    if bl:
      print()