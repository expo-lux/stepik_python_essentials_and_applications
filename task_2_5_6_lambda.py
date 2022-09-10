from functools import partial


def mod_func(yy, xx, m):
    return yy % xx == m


def mod_checker1(x, mod=0):
    return partial(mod_func, xx=x, m=mod)


mod_4 = partial(mod_func, x=4, mod=0)


def mod_3_a(y):
    return y % 3 == 0


mod_3_b = partial(mod_func, xx=3, m=0)

even = lambda x: x % 2 == 0

modp = lambda y, x, mod: y % x == mod

mod3 = lambda 3 , x, mod: 3 % x == mod

# def mod_checker(x, mod=0):
#     return partial(lambda yy, xx, modp: yy % xx == modp, xx=x, modp=mod)


def mod_checker(x, mod=0):
    return lambda y: y % x == mod

# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod


if __name__ == '__main__':
    # print(modp(15, 5, 0))
    # # print(mod_func(11, 3, 0))
    # # print(mod_3_a(11))
    # # print(mod_3_b(11))
    # mod_3 = mod_checker1(3)
    # #
    # print(mod_3(3))  # True
    # print(mod_3(4))  # False
    #
    # mod_3_1 = mod_checker1(3, 1)
    # print(mod_3_1(4))  # True

    print(mod3(3,0))

    print(mod_checker(3)(3))
    mod_3 = mod_checker(3)
    print(mod_3(3))  # True
    print(mod_3(4))  # False

