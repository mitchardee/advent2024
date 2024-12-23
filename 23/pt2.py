from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import *
from math import inf


lines = [x.strip().split('-') for x in open("testInput.txt").readlines()]
# lines = [x.strip().split('-') for x in open("input.txt").readlines()]

conns = defaultdict(set)
for [a,b] in lines:
    conns[a].add(b)
    conns[b].add(a)

@cache
def intersection(t):
    return reduce(
        lambda a, b: a & conns[b], 
        t, 
        set(conns.keys())
    )

@cache
def rec(t):
    if intersection(t):
        return max(
            (
                rec(
                    tuple(sorted((x, *t)))
                ) for x in intersection(t)
            ), 
            key=len
        )
    else:
        return t

print(','.join(rec(())))