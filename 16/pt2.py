from collections import Counter, defaultdict, deque
from heapq import *
from math import inf


# lines = [x.strip() for x in open("testInput.txt").readlines()]
lines = [x.strip() for x in open("input.txt").readlines()]

dirs = ((0,1), (-1,0), (0,-1), (1,0))

#Score, dir, r, c
h = [(0, 0, len(lines) - 2, 1, ((len(lines) - 2, 1),))]
goal = (1, len(lines[0]) - 2)
bestScorePath = defaultdict(set)
visited = {}
bestScore = inf

while h[0][0] <= bestScore:
    (s, d, r, c, path) = heappop(h)
    if (r, c) == goal:
        bestScore = s

    if (d, r, c) not in visited:
        visited[(d, r, c)] = s
        

    if visited[(d, r, c)] == s:
        bestScorePath[(d, r, c)] |= set(path)
        nr, nc = r + dirs[d][0], c + dirs[d][1]
        if lines[nr][nc] != '#':
            heappush(h, (s+1, d, nr, nc, path + ((nr,nc),)))
        heappush(h, (s + 1000, (d+1)%4, r, c, path))
        heappush(h, (s + 1000, (d-1)%4, r, c, path))
        

pathSpots = set()
for i in range(4):
    pathSpots |= bestScorePath[(i, goal[0], goal[1])]
print(len(pathSpots))