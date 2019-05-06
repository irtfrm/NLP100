class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def __repr__(self):
        return self.surface

def read_mecab(lines):
    ans = []

    for line in lines:
        if line == 'EOS\n':
            break
        x = line.split('\t')
        y = x[1].split(',')

        ans.append(Morph(x[0], y[6], y[0], y[1]))
    return ans

def read_cabocha(mecab, lines):
    ans = []
    sentence = []
    i = 0

    for line in lines:
        if line == '\n':
            break
        elif line == 'EOS\n':
            ans.append(sentence.copy())
            sentence = []
        else:
            while mecab[i].__repr__() in line:
                sentence.append(mecab[i])
                i += 1
    return ans


with open('neko.txt.mecab', 'r') as neko:
    lines = neko.readlines()

mec = read_mecab(lines)

with open('neko.txt.cabocha', 'r') as neko:
    lines = neko.readlines()

res = read_cabocha(mec, lines)

print(res[2])