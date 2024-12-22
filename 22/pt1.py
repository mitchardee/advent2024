from collections import Counter, defaultdict, deque
from functools import cache
from heapq import *
from math import inf


# lines = [int(x.strip()) for x in open("testInput.txt").readlines()]
lines = [int(x.strip()) for x in open("input.txt").readlines()]

ret = 0
for x in lines:
    for _ in range(2000):
        x = (x ^ (x*64)) % 16777216
        x = (x ^ (x // 32)) % 16777216
        x = (x ^ (x * 2048)) % 16777216
    print(x)
    ret += x
print(ret)