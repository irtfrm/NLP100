text1 = 'パトカー'
text2 = 'タクシー'

ans =''
for i in range(max(len(text1), len(text2))):
    if i < len(text1): ans += text1[i]
    if i < len(text2): ans += text2[i]

print(ans)