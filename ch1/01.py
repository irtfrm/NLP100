text = 'パタトクカシーー'

ans =''
for i, c in enumerate(text):
    if i % 2 == 1:
        ans += c

print(ans)