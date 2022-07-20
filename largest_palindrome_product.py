def is_palindrome(n):
    n = str(n)

    # If length is not even it is not a palindrome
    if len(n) % 2 != 0: return False

    # Check if reversed half of number is equal to first half of number
    return n[-1:int(len(n)/2)-1:-1] == n[0:int(len(n)/2)]


if __name__ == '__main__':
    max_palindrome = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if i*j > max_palindrome and is_palindrome(i*j):
                max_palindrome = i*j

    print(max_palindrome)