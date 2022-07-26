from sympy import divisor_count

def sum_of_first_n(n):
    return int(n*(n+1)/2)

if __name__ == "__main__":

    num = 1e4
    while divisor_count(sum_of_first_n(num)) <= 500:
        num += 1
    print(sum_of_first_n(num))