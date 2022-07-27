from num2words import num2words

def cnt_letters(n):
    return len(num2words(n).replace(' ','').replace('-',''))

if __name__ == "__main__":

    cnt = 0
    for i in range(1,1001):
        cnt += cnt_letters(i)

    print(cnt)