class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def __repr__(self):
        return '' + self.surface + ''

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
    
    def __repr__(self):
        return ''.join([morph.__repr__() for morph in self.morphs])
    
    def str_without_symbols(self):
        ans = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                ans += morph.surface
        return ans
    
    def include_pos(self, pos):
        return any([ morph.pos == pos for morph in self.morphs])
    
    def get_pos(self, pos):
        lst = []
        for morph in self.morphs:
                if morph.pos == pos:
                    lst.append(morph)
        return lst

def read_cabocha(lines):
    ans = []
    sentence = []
    chunk = None

    for line in lines:
        if line == '\n':
            break
        elif line == 'EOS\n':
            for i, ch in enumerate(sentence):
                if ch.dst > -1:
                    sentence[ch.dst].srcs.append(i)
            ans.append(sentence.copy())
            sentence = []
        elif line[:2] == '* ':
            x = line.split(' ')
            dst = int(x[2].strip('D'))
            chunk = Chunk([], dst, [])
            sentence.append(chunk)
        else:
            x = line.split('\t')
            y = x[1].split(',')

            chunk.morphs.append(Morph(x[0], y[6], y[0], y[1]))
    return ans

def gets_dot(sentence):
    ans = '''digraph {
    graph [fontname = "Hiragino Sans GB"];
    node [fontname = "Hiragino Sans GB"];
    edge [fontname = "Hiragino Sans GB"];
'''

    for chunk in sentence:
        ans += '    "%s"[shape=box];\n' % chunk.str_without_symbols()
        if chunk.dst > -1:
            dst_ch = sentence[chunk.dst]
            ans += '    "%s" -> "%s";\n' % (chunk.str_without_symbols(), dst_ch.str_without_symbols())
    ans += '}\n'
    return ans

with open('neko.txt.cabocha', 'r') as neko:
    lines = neko.readlines()

res = read_cabocha(lines)

for sentence in res:
    for j, chunk in enumerate(sentence):
        if not chunk.include_pos('名詞'): continue

        i = chunk
        l = []
        while True:
            l.append(i.str_without_symbols())
            if i.dst == -1: break
            i = sentence[i.dst]

        print(' -> '.join(l))