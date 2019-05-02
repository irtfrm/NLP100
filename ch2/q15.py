import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Argument error')
        exit(1)
    N = int(args[1])

    with open('hightemp.txt', 'r') as h:
        lines = h.readlines()

    for line in lines[len(lines) - min(N, len(lines)):]:
        print(line, end='')

#  [ tailコマンド ]
# ファイルを末尾から表示する。デフォルトの表示行数は10行。
#
# $ tail -n 3 hightemp.txt
# > 山梨県  大月    39.9    1990-07-19
# > 山形県  鶴岡    39.9    1978-08-03
# > 愛知県  名古屋  39.9    1942-08-02