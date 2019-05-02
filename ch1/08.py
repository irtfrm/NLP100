text = "This is a T-shirt."

a = ord('a')
z = ord('z')

ans =""
for c in text:
    if a <= ord(c) <= z:
        c = chr(219 - ord(c))
    ans += c

print(ans)