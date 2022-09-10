def even(x):
    return x % 2 == 0


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    k = map(even, l)
    d = filter(even, l)
    # print(type(k))
    # print(k)
    print(dir(k))
    print(dir(d))

    it = iter(k)
    while True:
        try:
            val = next(it)
            print(val)
        except StopIteration:
            break

    for i in k:
        print(i)

    for i in d:
        print(i)
