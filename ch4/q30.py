with open('neko.txt.mecab', 'r') as neko:
    lines = neko.readlines()
neko = []
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
        neko.append(sentence.copy())
        sentence = []

for i in range(500):
    for s in neko[i]:
        print(s['surface'], end=" ")
    print()