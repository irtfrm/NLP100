import datetime

start = 10
end = 13

today = str(datetime.date.today()).replace('-', '/')

for i in range(start, end):
    print("- [x] [問題%02d : %s](https://github.com/irtfrm/NLP100/blob/master/ch1/q%02d.py)" % (i, today, i))