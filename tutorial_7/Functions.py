def is_even(a):
    if a % 2 == 0:
        print("even no")
    else:
        print('Not even')


def find_max(a, b):
    if a > b:
        print("max is ", a)
    else:
        print("max is ", b)


def is_prime(a):
    c = 0
    for i in range(1, a + 1):
        if a % i == 0:
            c = c + 1
    return c == 2


def fac(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


if __name__ == '__main__':
    n = int(input('Enter a number \n'))
    r = int(input('Enter a number \n'))
    print(fac(n) / (fac(n - r) * fac(r)))
