
def convert_to_dict(lines):
    ans = []
    sentence = []

    for line in lines:
        if line == 'EOS\n':
            break
        x = line.split('\t')
        y = x[1].split(',')

        sentence.append({
            'surface' : x[0],
            'base' : y[6],
            'pos' : y[0],
            'pos1' : y[1]
        })

        if y[1] == '句点':
            ans.append(sentence.copy())
            sentence = []
        
    return ans


with open('neko.txt.mecab', 'r') as neko:
    lines = neko.readlines()

res = convert_to_dict(lines)

for snt in res:
    j = 0
    for  i, mor in enumerate(snt):
        if mor['pos'] == '名詞':
            j += 1
            if i == len(snt)-1:
                if j > 1: print(''.join([snt[k]['surface'] for k in range(i+1-j, i+1)]))
        elif j > 0:
            if j > 1: print(''.join([snt[k]['surface'] for k in range(i-j, i)]))
            j = 0