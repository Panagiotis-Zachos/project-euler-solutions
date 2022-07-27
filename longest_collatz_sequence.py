def collatz_fun(n):
    if str(n) in collatz_dict:
        return collatz_dict[str(n)]
    else:
        if n == 1:
            ret_val =  1
        elif n % 2 == 0:
            ret_val = collatz_fun(int(n/2)) + 1
        else:
            ret_val = collatz_fun(int(3*n + 1)) + 1
        collatz_dict[str(n)] = ret_val
        return ret_val

collatz_dict = {}
if __name__ == "__main__":
    t0 = time()
    coll_length = []
    for i in range(1, 1000001):
        coll_length.append(collatz_fun(i))

    print(max(collatz_dict, key=collatz_dict.get))