'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

if __name__ == "__main__":
    num = 20
    while True:
        flag = True
        for i in range(19,10,-1):
            if not(num % i == 0):
                flag = False
                break
        if flag: break
        num += 20

    print(num)
