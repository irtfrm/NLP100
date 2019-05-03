
with open('hightemp.txt', 'r') as h:
    lines = h.readlines()

lst = [line.split('\t') for line in lines]
lst.sort(key=lambda x:float(x[2]), reverse=True)

for l in lst:
    print('\t'.join(l), end='')

#  [ sortコマンド ]
# -k n : キーの設定
# -n : 数値としてソート
# -r : 降順でソート
# -t text : 区切り文字
#
# $ sort -k 3 -n -r -t $'\t' hightemp.txt
# > 高知県  江川崎  41      2013-08-12
# > 岐阜県  多治見  40.9    2007-08-16
# > ...
