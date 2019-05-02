import datetime

start, end = map(int, input().split())
end += 1

today = str(datetime.date.today()).replace('-', '/')

for i in range(start, end):
    N = i // 10 + 1
    print("- [x] [問題%02d : %s](https://github.com/irtfrm/NLP100/blob/master/ch%d/q%02d.py)" % (i, today, N, i))