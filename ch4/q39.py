import matplotlib.pyplot as plt

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

def uniq(lst):
    ans = []
    
    i = 1
    for j, l in enumerate(lst):
        if j == 0: continue
        if lst[j-1] == lst[j]:
            i += 1
            if j == len(lst)-1:
                ans.append([lst[j-1], i])
        else:
            ans.append([lst[j-1], i])
            i = 1

    return ans

with open('neko.txt.mecab', 'r') as neko:
    lines = neko.readlines()

res = []
for snt in convert_to_dict(lines):
    res.extend([mor['base'] for mor in snt])

res.sort()
ans = uniq(res)
ans.sort(key=lambda x:x[1], reverse=True)

left = [i+1 for i, a in enumerate(ans)]
right = [a[1] for a in ans]

plt.plot(left, right)

ax = plt.gca()
ax.spines['top'].set_color('none')

ax.set_xscale('log')
ax.set_yscale('log')

plt.grid(which="both")

plt.show()