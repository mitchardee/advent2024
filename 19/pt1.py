from collections import Counter, defaultdict, deque
from functools import cache
from heapq import *
from math import inf

lines = [x.strip() for x in open("input.txt").readlines()]

# lines = [x.strip() for x in open("testInput.txt").readlines()]

pieces = lines[0].split(", ")

@cache 
def rec(s: str):
    if not s:
        return True
    return any(rec(s[len(p):]) for p in pieces if s.startswith(p))

print(sum(bool(rec(lines[i])) for i in range(2, len(lines))))