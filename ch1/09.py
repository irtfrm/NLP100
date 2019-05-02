import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

ans = ""
for i, word in enumerate(text.split()):
    if i > 0: ans += " "
    l = len(word)
    if l > 4:
        ans += word[0]
        for w in random.sample(list(word[1:l-1]), l-2):
            ans += w
        ans += word[l-1]
    else:
        ans += word

print(ans)