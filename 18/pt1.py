from collections import Counter, defaultdict, deque
from heapq import *
from math import inf


# lines = [tuple(int(y) for y in x.strip().split(',')) for x in open("testInput.txt").readlines()]
# r = 7
# corrupted = set(lines[:12])

lines = [tuple(int(y) for y in x.strip().split(',')) for x in open("input.txt").readlines()]
r = 71
corrupted = set(lines[:1024])

# print(corrupted)

dirs = ((-1,0),(1,0),(0,-1),(0,1))
reached = {(0,0)}
steps = 0

while 1:
    l = len(reached)
    if (r-1, r-1) in reached:
        print(steps)
        break

    newR = set()
    for (x,y) in reached:
        for (dx, dy) in dirs:
            if 0 <= x+dx < r and 0 <= y+dy < r and (x+dx, y+dy) not in corrupted:
                newR.add((x+dx, y+dy))
    reached |= newR

    steps += 1

# for j in range(r):
#     for i in range(r):
#         print('#' if (i,j) in corrupted else 'O' if (i,j) in reached else '.', end='')
#     print()