import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Argument error')
        exit(1)
    N = int(args[1])

    with open('hightemp.txt', 'r') as h:
        lines = h.readlines()

    for i in range(len(lines)//N):
        m = min(len(lines), N)
        with open('q16/split%d.txt' % (i+1), 'w') as f:
            l = lines[m*i : m*(i+1)]
            f.write(''.join(l))
    
    if len(lines) % N > 0:
        i = len(lines)//N
        with open('q16/split%d.txt' % (i+1), 'w') as f:
            l = lines[N*i : len(lines)]
            f.write(''.join(l))


#  [ splitコマンド ]
# ファイルを分割する。デフォルトでは1000行ずつ分割。
#
# $ split -l 10 hightemp.txt
# $ head xaa
# > 高知県  江川崎  41      2013-08-12
# > 埼玉県  熊谷    40.9    2007-08-16
# > ...
# $ head xab
# > 群馬県  上里見  40.3    1998-07-04
# > 愛知県  愛西    40.3    1994-08-05
# > ...