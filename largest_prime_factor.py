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


if __name__ == '__main__':
    num = 600851475143
    # num = 5132455
    prime_factors = []

    current_check = 2

    while not(millerRabinTest(num, 7)):
        while not (num/current_check).is_integer():
            current_check += 1

        prime_factors.append(current_check)
        num = int(num / current_check)
        print(num)

    if millerRabinTest(num, 7): prime_factors.append(num)

    print(prime_factors)