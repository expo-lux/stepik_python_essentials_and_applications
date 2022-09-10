import re
import sys

if __name__ == "__main__":
    auto = True
    if auto:
        l=['\w    denotes    word    character',
        'sdfsdf\sdfsdf',
        'No    slashes    here']
    else:
        l = sys.stdin.readlines()
    print(*filter(lambda s: re.search(r'\\', s), l), sep='')
