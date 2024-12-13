from collections import defaultdict, deque
from functools import cache
from math import inf

lines = [x.split() for x in open("input.txt").readlines()]
tups = []
ret = 0

for i in range(0, len(lines), 4):
    tups.append(tuple(int (x) for x in (lines[i][2][2:-1], lines[i][3][2:], lines[i+1][2][2:-1], lines[i+1][3][2:], lines[i+2][1][2:-1], lines[i+2][2][2:])))

for t in tups:
    minCost = inf
    for i in range(101):
        if t[0] * i > t[4] or t[1] * i > t[5]:
            break
        b = (t[4] - i * t[0]) // t[2]
        if i * t[0] + b * t[2] == t[4] and i * t[1] + b * t[3] == t[5]:
            minCost = min(minCost, i * 3 + b)
    if minCost != inf:
        ret += minCost

print(ret)