def n_gram(lst, n):
    m = len(lst)
    ans = []

    for i in range(0, m-n+1):
        ans.append(lst[i:i+n])
    
    return ans

text = "I am an NLPer"
print(n_gram(text, 2))
print(n_gram(text.split(), 2))