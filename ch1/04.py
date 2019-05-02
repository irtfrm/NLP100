text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
lst = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dct = {}

for i, word in enumerate(text.split()):
    n = 1 if i+1 in lst else 2
    w = word[:n]
    dct[w] = i+1

print(dct)