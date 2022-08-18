from collections import Counter
from functools import reduce
from math import sqrt
from time import time
import random

PHI = (1 + 5 ** 0.5) / 2

def approx_fib(n):
    return PHI**n/sqrt(5)

def powerOfTwo(n):
    """
    Return which power of 2 n is with the remainder if not a perfect power of 2
    """
    r = 0
    d = n
    while(d%2==0):
        r += 1
        d >>= 1
    assert(2**r * d == n)
    return r, d


def miller_rabin(n, k=7):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.

    k is the number of trials that should be performed.
    Normally k=7 is more than enough
    """
    if n <= 3:
        return False
    r, d = powerOfTwo(n-1)

    for _ in range(k):
        rInt = random.randint(2, n-2)
        x = pow(rInt,d,n)

        if x == 1 or x == n - 1:
            continue
        flag = 0

        for _ in range(r-1):
            x = pow(x,2,n)

            if x == n - 1:
                flag = 1
                break

        if flag == 1:
            continue
        else:
            return False
    return True


def get_prime_factors(num):
    """
    Lightning-fast prime-factor list generator of num
    """
    prime_factors = []

    current_check = 2

    while not(miller_rabin(num, 7)) and num != 1:
        while not (num/current_check).is_integer() and num != 1:
            current_check += 1
            
        prime_factors.append(current_check)
        num = int(num / current_check)
    if miller_rabin(num, 7): prime_factors.append(num)

    return prime_factors


def prime_factor_multiplicity(num):
    prime_factors = get_prime_factors(num)
    for (k,v) in Counter(prime_factors).items():
        yield (k,v)


def divisor_gen(n):
    """
    Generator of perfect divisors of n
    """
    factors = list(prime_factor_multiplicity(n))
    nfactors = len(factors)

    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


if __name__ == '__main__':
    num = 2893751023948627304498257532342
    t0 = time()
    # print((get_prime_factors(num)))
    prime_factors = get_prime_factors(num)
    for (k,v) in prime_factor_multiplicity(num):
        print(k,v)
    print(time() - t0)