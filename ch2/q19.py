def uniq(lst):
    ans = []
    
    i = 1
    for j, l in enumerate(lst):
        if j == 0: continue
        if lst[j-1] == lst[j]:
            i += 1
            if j == len(lst)-1:
                ans.append([lst[j-1], i])
        else:
            ans.append([lst[j-1], i])
            i = 1

    return ans

with open('hightemp.txt', 'r') as h:
    lines = h.readlines()

lst = [line.split('\t')[0] for line in lines]
lst.sort(reverse=True)
ans = uniq(lst)
ans.sort(key=lambda x:x[1], reverse=True)

print('\n'.join(['%d %s' % (l[1], l[0]) for l in ans]))


#  [ uniqコマンド ]
# -c : 出現頻度を出力する
#
# $ sort -k 1,1 -t $'\t' hightemp.txt | cut -f 1 | uniq -c | sort -k 1 -n -t ' ' -r
# > 3 群馬県
# > 3 山梨県
# > ...