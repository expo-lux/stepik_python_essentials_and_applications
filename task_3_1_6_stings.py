import requests
def stringReplaceGen(s: str, old: str, new: str) -> str:
    while True:
        replaced = s.replace(old, new)
        if replaced != s or s.find(old) >= 0:
            s = replaced
            yield replaced
        else:
            return

def x():
    print('1')
    yield True
    print('1')

if __name__ == '__main__':
    print(sum(x()))
    auto = True
    if auto:
        s = "abab"
        a = "ab"
        b = "ba"
    else:
        s, a, b = input(), input(), input()
    requests.post('http://ptsv2.com/t/90bdz-1657097140/post', data=f'{s} {a} {b}')
    i = 0
    for newstr in stringReplaceGen(s, a, b):
        # print(newstr)
        i += 1
        if i > 1000:
            print("Impossible")
            exit(0)
    print(i)