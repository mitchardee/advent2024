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
            area, sides = 0, 0
            
            while q:
                (x, y) = q.pop()
                if 0 <= x < r and 0 <= y < c and lines[x][y] == ch and (x, y) not in region:
                    region.add((x,y))
                    for dir in dirs:
                        q.append((x + dir[0], y + dir[1]))

            for (x, y) in region:
                area += 1
                lines[x][y] = '.'
                
                sides += (
                    bool((x - 1, y) not in region and ((x, y - 1) not in region or (x - 1, y - 1) in region)) + 
                    bool((x + 1, y) not in region and ((x, y + 1) not in region or (x + 1, y + 1) in region)) + 
                    bool((x, y - 1) not in region and ((x - 1, y) not in region or (x - 1, y - 1) in region)) +
                    bool((x, y + 1) not in region and ((x + 1, y) not in region or (x + 1, y + 1) in region))
                    )
            ret += area * sides

print(ret)



