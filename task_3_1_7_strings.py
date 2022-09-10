if __name__ == '__main__':
    auto = True
    if auto:
        s, t, res = "abababa", "aba", set()
    else:
        s, t, res = input(), input(), set()


    def indexer(s, t):
        index = 0
        while True:
            pos = s.find(t, index)
            if pos == -1:
                return
            index = pos + 1
            yield pos

    print(len(list(indexer(s, t))))

    # if t in s:
    #     for i in range(len(s)):
    #         index = s.find(t, i)
    #         if index >= 0:
    #             res.add(index)
    #         else:
    #             break
    # print(len(res))
