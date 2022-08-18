from time import time
import itertools

if __name__ == "__main__":
    """
    Definetely not the most efficent solution, but I couldn't resist the 1-liner solution this time
    """
    t0 = time()
    perms = [''.join(map(str, i)) for i in itertools.permutations([0,1,2,3,4,5,6,7,8,9], 10)]
    print(perms[999999])

    print(time() - t0)