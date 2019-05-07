class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def __repr__(self):
        return '"' + self.surface + '"'


def read_cabocha(lines):
    ans = []
    sentence = []

    for line in lines:
        if line == '\n':
            break
        elif line == 'EOS\n':
            ans.append(sentence.copy())
            sentence = []
        elif line[:2] == '* ':
            continue
        else:
            x = line.split('\t')
            y = x[1].split(',')

            sentence.append(Morph(x[0], y[6], y[0], y[1]))
    return ans


with open('neko.txt.cabocha', 'r') as neko:
    lines = neko.readlines()

res = read_cabocha(lines)

print(res[2])