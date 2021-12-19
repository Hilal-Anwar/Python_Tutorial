def fun(a, b, l):
    if l >= 1:
        print(fun(b, a + b, l - 1))
    return a + b


fun(0, 1, 10)
