from collections import deque

prev_fib = deque([0, 1, 111])
even_fib_nums = []

while True:
    prev_fib[2] = prev_fib[0] + prev_fib[1]
    if prev_fib[2] > 4e6: break
    if prev_fib[2] % 2 == 0: even_fib_nums.append(prev_fib[2])
    prev_fib.rotate(-1)

print(sum(even_fib_nums))