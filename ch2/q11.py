with open('hightemp.txt', 'r') as f:
    for line in f:
        print(line.replace('\t', ' '), end='')

#  [ sedコマンド ]
# 正規表現で文字列を置換できる。"cat in.txt | sed -e 's/abc/ABC/g' > out.txt"など。
# tab文字の入力が謎で手間取った。
#  参考URL : https://mattintosh.hatenablog.com/entry/2013/01/16/143323
#
# $ sed -e $'s/\t/ /g' ./hightemp.txt
# > 高知県 江川崎 41 2013-08-12
# > 埼玉県 熊谷 40.9 2007-08-16
# > ...
#
#  ---
#
#  [ trコマンド ]
# シンプルに文字列を置換するコマンド。
#
# $ cat hightemp.txt | tr '\t' ' '
# > 高知県 江川崎 41 2013-08-12
# > 埼玉県 熊谷 40.9 2007-08-16
# > ...