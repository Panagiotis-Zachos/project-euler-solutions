from helper_functions import divisor_gen
from time import time

"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.
"""

def abundant_check(num):
    divisor_sum = sum(list(divisor_gen(num))[:-1])
    if divisor_sum > num:
        # Number is abundant
        return 1
    elif divisor_sum == num:
        # Number is perfect
        return 0
    else:
        # Number is deficient
        return -1


def abundant_sum(num, abundant_sieve):
    # Return True when num can be written as sum of 2 abundant numbers
    for i in range(1, num):
        if abundant_sieve[i - 1] + abundant_sieve[num - i - 1] == 2:
            return True
    return False


if __name__ == "__main__":

    abundant_sieve = [False]*28123

    t0 = time()
    for i in range(2, 28123):
        abundant_check_result = abundant_check(i)
        if abundant_check_result == 1:
            # All multiples of abundant numbers are abundant
            mult = 1
            while mult * i < 28123 and not(abundant_sieve[mult * i - 1]):
                abundant_sieve[mult * i - 1] = True
                mult += 1
        elif abundant_check_result == 0:
            # Multiples of perfect numbers, exlcuding said number, are abundant
            mult = 2
            while mult * i < 28123 and not(abundant_sieve[mult * i - 1]):
                abundant_sieve[mult * i - 1] = True
                mult += 1
    
    non_abundant_sum = 0
    for i in range(1, 28123):
        if not abundant_sum(i, abundant_sieve):
            non_abundant_sum += i

    print(time()-t0)
    print(non_abundant_sum)