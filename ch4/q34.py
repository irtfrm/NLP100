
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
    for  i, mor in enumerate(snt):
        if mor['pos'] == '名詞' and i > 1:
            if snt[i-1]['surface'] == 'の' and snt[i-2]['pos'] == '名詞':
                print(snt[i-2]['surface'] + 'の' + snt[i]['surface'])