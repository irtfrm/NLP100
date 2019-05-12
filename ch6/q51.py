import re
import sys

def main(argv):
    ans = []
    for line in argv:
        l = re.findall(r'([a-zA-Z]+)[.,:;!?]?(?:(?:\s*?)|(?:$))', line)
        l.append('')
        ans.extend(l)

    for line in ans:
        print(line)

if __name__ == "__main__":
    main(sys.stdin)