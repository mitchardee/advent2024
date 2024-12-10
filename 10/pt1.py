from collections import defaultdict
from functools import cache

lines = [[int(k) for k in x.strip()] for x in open("input.txt").readlines()]
dirs = ((-1,0),(1,0),(0,-1),(0,1))
ret = 0
r, c = len(lines), len(lines[0])

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val == 0:
            q = {(i, j)}
            nextQ = set()
            for k in range(1,10):
                for (x, y) in q:
                    for dir in dirs:
                        newX, newY = x + dir[0], y + dir[1]
                        if 0 <= newX < r and 0 <= newY < c and lines[newX][newY] == k:
                            nextQ.add((newX, newY))
                q = nextQ
                nextQ = set()
            ret += len(q)

print(ret)
