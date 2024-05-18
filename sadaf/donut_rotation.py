

import math


def fill_array(a, size, b):
    for i in range(0, size):
        a.append(b)


def draw_donut():
    ab = 0.0
    cd = 0.0
    z = []
    b = []
    so = 0
    wer = 0
    while True:
        b.clear()
        z.clear()
        fill_array(b, 1761, ' ')
        fill_array(z, 1761, 0.0)
        j = 0.0
        while 6.28 > j:
            i = 0.0
            while 6.28 > i:
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(ab)
                f = math.sin(j)
                g = math.cos(ab)
                h = d + 2
                de = 1 / (c * h * e + f * g + 5)
                li = math.cos(i)
                m = math.cos(cd)
                n = math.sin(cd)
                t = c * h * g - f * e
                x = int(40 + 30 * de * (li * h * m - t * n))
                y = int(12 + 15 * de * (li * h * n + t * m))
                o = x + 80 * y
                wer = wer + 1
                nm = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - li * d * n))
                if 22 > y > 0 and 0 < x < 80 and de > z[o]:
                    so = so + 1
                    z[o] = de
                    art = ['.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@']
                    b[o] = art[max(nm, 0)]
                i = i + 0.02
            j = j + 0.07
        st = ' '
        print("\u001b[H", end='')
        for k in range(0, 1761):
            if (k % 80) > 0:
                st = st + b[k]
            else:
                st = st + '\n'
        ab = ab + 0.12
        cd = cd + 0.06
        print(st, end='')


if __name__ == '__main__':
    draw_donut()
