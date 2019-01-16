from itertools import takewhile
from time import clock

from eulerlib import fibonacci

def fibonacci_until(limit):
    return takewhile(lambda x: x <= limit, fibonacci())

t0 = clock()
fibs = fibonacci_until(4000000)
print(sum(x for x in fibs if x & 1 == 0))
t1 = clock()
print(t1-t0)