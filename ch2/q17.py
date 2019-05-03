
with open('hightemp.txt', 'r') as h:
    lines = h.readlines()

lst = []
for line in lines:
    t = line.split('\t')[0]
    if not t in lst:
        lst.append(t)

print('\n'.join(lst))

#  [ sortコマンド ]
# ファイルを並べ替えるコマンド。
# '和歌山県'の位置から察するに、文字列を並び替える順序が微妙に辞書式順序と異なる(長さ->辞書式でソートしてる)。
#
# $ sort -u -k 1,1 -t $'\t' hightemp.txt | cut -f 1
# > 千葉県
# > 埼玉県
# > ...
#
#  [ uniqコマンド ]
# ソート済みファイルから重複行を除く。'uniq in.txt'など。
#
# $ sort -k 1,1 -t $'\t' hightemp.txt | cut -f 1 | uniq
# > 千葉県
# > 埼玉県
# > ...