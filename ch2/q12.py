with open('hightemp.txt', 'r') as h:
    lines = h.readlines()

l0 = []
l1 = []
for line in lines:
    r = line.split('\t')[:2]
    l0.append(r[0])
    l1.append(r[1])

with open('col1.txt', 'w') as c1:
    c1.write('\n'.join(l0))

with open('col2.txt', 'w') as c2:
    c2.write('\n'.join(l1))

#  [ cutコマンド ]
# テキストファイルを横方向に分割する。"cut -f 1-2 -d ":" in.txt > out.txt"など。
# -fオプションを指定する場合、デフォルトではtab文字が区切り文字に指定される。すなわち-dオプションは指定しなくてよい。
#
# $ cut -f 1  hightemp.txt
# > 高知県
# > 埼玉県
# > ...