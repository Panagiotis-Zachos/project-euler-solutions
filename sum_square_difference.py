def sum_of_first_n(n):
    return int(n*(n+1)/2)


def sum_of_first_n_squares(n):
    return int((n*(n+1)*(2*n+1)) / 6)


if __name__ == "__main__":
    print(sum_of_first_n(100)**2 - sum_of_first_n_squares(100))
