from math import floor
from time import time

m3 = [ i*3 for i in range(floor(1000 / 3) + 1)]
m5 = [ i*5 for i in range(floor(1000 / 5))]

print(sum(set(m3).union(set(m5))))