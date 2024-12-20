from collections import Counter, defaultdict, deque
from heapq import *
from math import inf


# lines = [list(x.strip()) for x in open("testInput.txt").readlines()]
# savings = 8
lines = [list(x.strip()) for x in open("input.txt").readlines()]
savings = 100

M, N = len(lines), len(lines[0])

dirs = ((0,1), (-1,0), (0,-1), (1,0))
S = next((i, line.index('S')) for i, line in enumerate(lines) if 'S' in line)
E = next((i, line.index('E')) for i, line in enumerate(lines) if 'E' in line)

sDists = [[inf] * N for _ in range(M)]
toVisit = {S}
dist = 0

while toVisit:
    visitNext = set()

    for (i, j) in toVisit:
        if sDists[i][j] == inf and lines[i][j] != '#':
            sDists[i][j] = dist
            for (dx, dy) in dirs:
                visitNext.add((i+dx, j+dy))

    dist += 1
    toVisit = visitNext


eDists = [[inf] * N for _ in range(M)]
toVisit = {E}
dist = 0

while toVisit:
    visitNext = set()

    for (i, j) in toVisit:
        if eDists[i][j] == inf and lines[i][j] != '#':
            eDists[i][j] = dist
            for (dx, dy) in dirs:
                visitNext.add((i+dx, j+dy))
                
    dist += 1
    toVisit = visitNext

totalDist = sDists[E[0]][E[1]]
ret = 0

for i in range(1, M-1):
    for j in range(1, N-1):
        if lines[i][j] == '#':
            bestStart = min(sDists[i+dx][j+dy] for (dx, dy) in dirs)
            for (dx, dy) in dirs:
                i2, j2 = i+dx, j+dy
                if eDists[i2][j2] + bestStart + 2 <= totalDist - savings:
                    ret += 1

print(ret)
