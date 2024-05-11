import time
from math import ceil, sqrt


def pythagorean_triplets(n):
    count = 0
    # calculate spf array
    spf = eratostheneseieve(2 * (n - int(sqrt(2 * n - 1))))

    # looping for every values of 2*b
    for b2 in range(4, 2 * (n - int(sqrt(2 * n - 1))), 2):

        # calculates reduced factor of 2*b
        gamma = get_reduced_factorization(b2, spf)

        # for findin all triplets from 2*b
        for i in range(1, int(sqrt(b2 * ((b2 // 2) - 1))) // gamma + 1):
            i *= gamma
            sqVal = i * i
            q = sqVal // b2
            if q + i + (b2 // 2) > n:
                break
            else:
                x = q + i
                # print((x, (b2 // 2) + i, x + (b2 // 2)))
                count += 1
    print("Number of pythagorean triplets are ", count)


def eratostheneseieve(n: int) -> list:
    '''
    Calculating SPF (Smallest Prime Factor) for every number till N.
    Time Complexity : O(NloglogN)
    '''
    n += 1
    # stores smallest prime factor for every number
    spf = [*range(n)]

    # separately marking spf for every even number as 2
    for i in range(4, n, 2):
        spf[i] = 2
    for i in range(3, ceil(sqrt(n))):
        # checking if i is prime
        if (spf[i] == i):
            # marking SPF for all numbers divisible by i
            for j in range(i * i, n, i):
                # marking spf[j] if it is not previously marked
                if (spf[j] == j):
                    spf[j] = i
    return spf


def get_reduced_factorization(n: int, spf: list) -> int:
    """
    counts repetition of each prime from prime factorisation of N
    using trial method upon spf list, and calculating the ceil of
    half of all prime's powers (pow(p, ceil(a / 2))) and multiplying
    them together.
    """
    gamma = 1
    while (n != 1):
        # keep a prime in prev variable
        prev = spf[n]
        # for counting the power
        c = 0
        # counts power of a prime
        while spf[n] == prev:
            c += 1
            n //= spf[n]
        # multiplies the half ceil of power on primes
        gamma *= pow(prev, ceil(c / 2))
        prev = spf[n]
    return gamma


if __name__ == '__main__':
    a = time.time_ns()
    pythagorean_triplets(500000)
    print((time.time_ns()-a)/100000)
