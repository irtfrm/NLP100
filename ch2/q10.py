with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

print(len(lines))
# 24


#  [ wcコマンド ]
# 出力は行数、文字数、バイト数を表している
#
# $ wc hightemp.txt
# >      24      98     813 hightemp.txt