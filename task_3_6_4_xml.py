import sys
from xml.etree import ElementTree
from collections import defaultdict


def traverse(num, element, dic):
    for child in element:
        color = child.attrib['color']
        dic[color] += num
        traverse(num + 1, child, dic)


if __name__ == "__main__":
    autoTest = False
    if autoTest:
        s = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
    else:
        inp, s = sys.stdin, ''
        for i in inp:
            s += i
    root = ElementTree.fromstring(s)
    root.findall()
    dic = defaultdict(int)
    color = root.attrib['color']
    dic[color] = 1
    traverse(2, root, dic)
    print(f"{dic['red']} {dic['green']} {dic['blue']}")
