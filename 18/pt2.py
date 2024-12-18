from collections import Counter, defaultdict, deque
from heapq import *
from math import inf

dirs = ((-1,0),(1,0),(0,-1),(0,1))

# lines = [tuple(int(y) for y in x.strip().split(',')) for x in open("testInput.txt").readlines()]
# n = 7

lines = [tuple(int(y) for y in x.strip().split(',')) for x in open("input.txt").readlines()]
n = 71

l, r = 0, len(lines)

while l+1 < r:
    m = (l+r)//2
    reached = {(0,0)}
    lastReached = {(0,0)}
    corrupted = set(lines[:m+1])

    while 1:
        #If the current set of corrupted spaces still allows for traversal
        if (n-1, n-1) in reached:
            l = m
            break

        newR = set()
        for (x,y) in lastReached:
            for (dx, dy) in dirs:
                x2, y2 = x+dx, y+dy
                if 0 <= x2 < n and 0 <= y2 < n and (x2, y2) not in corrupted and (x2, y2) not in reached:
                    newR.add((x2, y2))
        
        #Only traverse newly reached spaces for efficiency
        lastReached = newR
        reached |= newR

        #If all reachable spaces have been reached, traversal is impossible
        if len(newR) == 0:
            r = m
            break

print(lines[r])