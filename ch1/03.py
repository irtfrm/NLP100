text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = text.replace(',','').replace('.','')
l = [ len(word) for word in text.split()]

print(l)