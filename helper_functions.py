import random

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

    while not(miller_rabin(num, 7)):
        while not (num/current_check).is_integer():
            current_check += 1

        prime_factors.append(current_check)
        num = int(num / current_check)

    if miller_rabin(num, 7): prime_factors.append(num)

    return prime_factors

if __name__ == '__main__':
    num = 128314298301230219287319203812302123111114123245124354123124412341234342353464350000000
    print(get_prime_factors(num))