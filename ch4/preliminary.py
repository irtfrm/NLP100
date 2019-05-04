import MeCab

with open('neko.txt', 'r') as neko:
    lines = neko.read()

mecab = MeCab.Tagger("/usr/local/lib/mecab/dic/mecab-ipadic-neologd")

with open('neko.txt.mecab', 'w') as neko:
    neko.write(mecab.parse(lines))