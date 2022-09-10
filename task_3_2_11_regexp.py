import re
import sys

if __name__ == "__main__":
    auto = True
    if auto:
        inp = 'blabla is a tandem repetition\n123123 is good too\ngo go\naaa'.split('\n')
    else:
        inp = sys.stdin
    for line in inp:
        if re.search(r'\b(\w{2,})\1\b', line.strip()):
            print(line)
