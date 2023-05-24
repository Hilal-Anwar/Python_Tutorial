def get_hcf(a, b):
    mx = max(a, b)
    mi = min(a, b)
    while mx % mi != 0:
        temp = mi
        mi = mx % mi
        mx = temp
    return mi


def c_factor(a, b, c):
    return get_hcf(get_hcf(a, b), c)


def _generate_pythagorean_triplet(start, end):
    m = (start - 1) / 2
    n = m + 1
    cr = 0
    while (n * n + m * m) <= end:
        i = n
        while (m * m + i * i) <= end:
            a = i * i - m * m
            b = 2 * m * i
            c = m * m + i * i
            k = 1
            if c_factor(a, b, c) == 1:
                while c * k <= end:
                    k += 1
                    cr += 1
            i += 1
        m = m + 1
        n = n + 1
    print("Number of Pythagorean triplet", cr)


if __name__ == '__main__':
    _generate_pythagorean_triplet(3, 2000000)
