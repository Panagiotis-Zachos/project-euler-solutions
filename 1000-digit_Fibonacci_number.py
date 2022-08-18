from math import log10, sqrt
from time import time


if __name__ == "__main__":
    """
    Find the index of the first fibonacci number with more than 1000 digits.
    This is based upon the fibonacci number approximation function:
    F(n) = PHI ** n / sqrt(5)
    and the fact that by taking the int(log10(F)) + 1 we can easily count the digits of the result

    Completes in 0.0159 seconds on i5-10gen Dell XPS13
    """
    PHI = (1 + 5 ** 0.5) / 2
    t0 = time()
    fib_num = 1
    while int(fib_num * log10(PHI) - log10(sqrt(5)))+1 < 1000:
        fib_num += 1
    print(fib_num)
    print('Time to complete: ' + str(time() - t0))