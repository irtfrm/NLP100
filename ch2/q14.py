import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Argument error')
        exit(1)
    N = int(args[1])

    with open('hightemp.txt', 'r') as h:
        lines = h.readlines()
    
    for line in lines[:min(N, len(lines))]:
        print(line, end='')

#  [ headコマンド ]
# ファイルを先頭から表示する。デフォルトの表示行数は10行。
#
# $ head -n 3 hightemp.txt
# > 高知県  江川崎  41      2013-08-12
# > 埼玉県  熊谷    40.9    2007-08-16
# > 岐阜県  多治見  40.9    2007-08-16