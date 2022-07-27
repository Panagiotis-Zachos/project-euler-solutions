import numpy as np

def fast_pow(n,p):
    if p == 1:
        return n
    elif p % 2 == 0:
        return fast_pow(n*n, int(p/2))
    else:
        return fast_pow(n*n, int((p-1)/2)) * n

if __name__ == "__main__":
    num = np.array(list(map(int, list(str(fast_pow(2,1000))))))
    print(np.sum(num))

