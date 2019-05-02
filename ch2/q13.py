with open('col1.txt', 'r') as c1:
    l1 = [ l.rstrip('\n') for l in c1.readlines() ]

with open('col2.txt', 'r') as c2:
    l2 = [ l.rstrip('\n') for l in c2.readlines() ]

with open('merge.txt', 'w') as m:
    for i in range(len(l1)):
        m.write(l1[i] + '\t' + l2[i] + '\n')


#  [pasteコマンド]
# 複数のファイルをタブ区切りでくっ付ける。
#
# $ paste col1.txt col2.txt
# > 高知県  江川崎
# > 埼玉県  熊谷
# > ...