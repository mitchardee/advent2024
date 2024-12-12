from collections import defaultdict, deque
from functools import cache

lines = [[ch for ch in x.strip()] for x in open("input.txt").readlines()]
dirs = ((-1,0),(1,0),(0,-1),(0,1))
r, c = len(lines), len(lines[0])
ret = 0

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch != '.':
            region = set()
            q = [(i,j)]
            area, perimeter = 0, 0
            while q:
                # print(q)
                (x, y) = q.pop()
                if 0 <= x < r and 0 <= y < c and lines[x][y] == ch and (x, y) not in region:
                    region.add((x,y))
                    for dir in dirs:
                        q.append((x + dir[0], y + dir[1]))

            for (x, y) in region:
                area += 1
                perimeter += 4
                lines[x][y] = '.'
                for dir in dirs:
                    if (x + dir[0], y + dir[1]) in region:
                        perimeter -= 1
            ret += area * perimeter

print(ret)



