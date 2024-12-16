from collections import Counter, defaultdict, deque
from heapq import *
from math import inf


# lines = [x.strip() for x in open("testInput.txt").readlines()]
lines = [x.strip() for x in open("input.txt").readlines()]

dirs = ((0,1), (-1,0), (0,-1), (1,0))

#Score, dir, r, c
h = [(0, 0, len(lines) - 2, 1)]
goal = (1, len(lines[0]) - 2)
visited = set()

while 1:
    (s, d, r, c) = heappop(h)
    if (r, c) == goal:
        print (s)
        break
    if (d, r, c) not in visited:
        visited.add((d, r, c))
        nr, nc = r + dirs[d][0], c + dirs[d][1]
        if lines[nr][nc] != '#':
            heappush(h, (s+1, d, nr, nc))
        heappush(h, (s + 1000, (d+1)%4, r, c))
        heappush(h, (s + 1000, (d-1)%4, r, c))

