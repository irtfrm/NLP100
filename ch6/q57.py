import xml.etree.ElementTree as ET

def gets_dot(tokens, deps):
  ans = 'digraph {\n'

  ans += '    token%s [label="%s"];\n' % (0, 'ROOT')
  for token in tokens:
    ans += '    token%s [shape=box, label="%s"];\n' % (token['id'], token['word'])
  for dep in deps:
    ans += '    token%s -> token%s;\n' % (dep['governor'], dep['dependent'])

  ans += '}\n'
  return ans

with open('nlp.txt.xml', 'r') as f:
    lines = ''.join(f.readlines()) 
root = ET.fromstring(lines)

tokens = []
deps = []
for sentence in root.findall('./document/sentences/sentence'):
  lst = []
  for token in sentence[0]:
    lst.append({
      'id' : int(token.attrib['id']),
      'word' : token[0].text
    })
  tokens.append(lst)

  lst = []
  for dep in sentence[2]:
    lst.append({
      'governor' : int(dep[0].attrib['idx']),
      'dependent' : int(dep[1].attrib['idx']),
    })
  deps.append(lst)

i = 0
print(gets_dot(tokens[i], deps[i]))