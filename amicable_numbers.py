from functools import reduce
from helper_functions import prime_factor_multiplicity, miller_rabin
import numpy as np

def divisorGen(n):
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


def function_d(num):
    return int(np.sum(list(divisorGen(num))[:-1]))

if __name__ == "__main__":

    amicable_sum = 0
    for current_num in range(4,10000 + 1):
        if miller_rabin(current_num): continue
        amicable_pair = function_d(current_num)

        # Normally another check for amicable_pair <= 10000 is required but no such
        # pair exists
        if amicable_pair != current_num and current_num ==  function_d(amicable_pair):
            amicable_sum += amicable_pair + current_num
            print(current_num, amicable_pair)

    # Silly way of solving the easily solvable problem of counting the pairs twice
    print(int(amicable_sum / 2))