import re
import sys
from nltk import stem

stemmer = stem.PorterStemmer()

def main(argv):
    ans = []
    for word in argv:
        l = stemmer.stem(word.strip('\n'))
        ans.append(l)

    for line in ans:
        print(line)

if __name__ == "__main__":
    main(sys.stdin)