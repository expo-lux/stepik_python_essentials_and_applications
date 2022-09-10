import itertools
def primes():
    val = 2
    while True:
        simple = True
        for i in range(2, val):
            if val % i == 0:
                simple = False
                break
        if simple:
            yield val
        val += 1

# it = iter(primes())
# for k in range(4):
#     print(next(it))

for i in primes():
    print(i)
    if i >= 4:
        break


# print(list(itertools.takewhile(lambda x : x <= 7, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]