import sys
import re
if __name__ == "__main__":
    auto = True
    if auto:
        inp = 'this is a text\n"this\' !is. ?n1ce,'.split('\n')
    else:
        inp = sys.stdin
    for line in inp:
        print(re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line.strip()))
