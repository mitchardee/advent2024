from collections import Counter, defaultdict, deque
from functools import cache
from heapq import *
from math import inf


# lines = [x.strip().split('-') for x in open("testInput.txt").readlines()]
lines = [x.strip().split('-') for x in open("input.txt").readlines()]

conns = defaultdict(set)
for [a,b] in lines:
    conns[a].add(b)
    conns[b].add(a)

tGroups = set()
for k in conns.keys():
    if k[0] == 't':
        for v in conns[k]:
            for x in conns[k] & conns[v]:
                tGroups.add(tuple(sorted((k,v,x))))

print(len(tGroups))
