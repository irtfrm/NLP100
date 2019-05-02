
def n_gram(lst, n):
    m = len(lst)
    ans = []

    for i in range(0, m-n+1):
        ans.append(lst[i:i+n])
    
    return ans

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))

print('X = ',end='')
print(X)

print('Y = ',end='')
print(Y)

print('X&Y = ',end='')
print(X & Y)

print('X|Y = ',end='')
print(X | Y)

print('X-Y = ',end='')
print(X - Y)

if 'se' in X:
    print("'se' in X: YES")
else:
     print("'se' in X: NO")

if 'se' in Y:
    print("'se' in Y: YES")
else:
     print("'se' in Y: NO")