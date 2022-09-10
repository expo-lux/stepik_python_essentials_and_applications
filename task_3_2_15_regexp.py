import re
import subprocess
import sys
if __name__ == '__main__':
    auto_test = False
    if auto_test:
        enc = b'attraction\nbuzzzz'
    else:
        for line in sys.stdin:
            print(re.sub(r'(\w)\1+', r'\1', line.strip()))
    # s = subprocess.check_output(["tr", "-s", "'[:alpha:]'"], input=enc)
    # print(s.decode("utf-8"))
