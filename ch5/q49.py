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
    lst = []
    for j, chunk in enumerate(sentence):
        if not chunk.include_pos('名詞'): continue

        i = chunk
        l = []
        while True:
            l.append(i)
            if i.dst == -1: break
            i = sentence[i.dst]
        lst.append(l)


    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j][0] in lst[i]:
                n = lst[i].index(lst[j][0])
                ans = [chunk.str_without_symbols() for chunk in lst[i][:n+1]]

                ans[0] = ans[0].replace(lst[i][0].get_pos('名詞')[0].surface, 'X')
                ans[n] = ans[n].replace(lst[i][n].get_pos('名詞')[0].surface, 'Y')

                print(' -> '.join(ans))
            else:
                l1 = list(reversed(lst[i]))
                l2 = list(reversed(lst[j]))

                n = 0
                while n < min(len(l1), len(l2)):
                    n += 1
                    if l1[n] != l2[n]:
                        break

                a1 = list(reversed(l1[n:]))
                a1 = [chunk.str_without_symbols() for chunk in a1]
                a1[0] = a1[0].replace(lst[i][0].get_pos('名詞')[0].surface, 'X')
                a2 = list(reversed(l2[n:]))
                a2 = [chunk.str_without_symbols() for chunk in a2]
                a2[0] = a2[0].replace(lst[j][0].get_pos('名詞')[0].surface, 'Y')

                text = ' -> '.join(a1) + ' | ' + ' -> '.join(a2) + ' | ' + l1[n-1].str_without_symbols()
                print(text)