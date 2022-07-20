'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math
import random

def powerOfTwo(n):
    r = 0
    d = n
    while(d%2==0):
        r += 1
        d >>= 1
    assert(2**r * d == n)
    return r, d


def millerRabinTest(n, k):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
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


if __name__ == "__main__":
    count = 0
    num = 3
    while count < 10001-2:
        if millerRabinTest(num, 7):
            count += 1
        num += 2

    print(num-2)