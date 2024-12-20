from collections import Counter, defaultdict, deque
from functools import cache
from heapq import *
from math import inf

lines = [x.strip() for x in open("input.txt").readlines()]

# lines = [x.strip() for x in open("testInput.txt").readlines()]

pieces = lines[0].split(", ")
ret = 0

for s in lines[2:]:
    dp = [0] * (len(s)+1)
    dp[0] = 1
    for i in range(len(dp) - 1):
        if dp[i]:
            for p in pieces:
                if s[i:].startswith(p):
                    dp[i + len(p)] += dp[i]
    ret += dp[-1]

print(ret)