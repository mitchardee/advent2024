from collections import Counter, defaultdict, deque
from functools import cache, reduce
from math import inf
from operator import mul


# lines = [x.strip() for x in open("testInput.txt").readlines()]
lines = [x.strip() for x in open("input.txt").readlines()]

dirs = {'^': (-1,0), '<': (0,-1), '>': (0,1), 'v':(1,0)}

d = False
start = None
dirList = []
map = []


for i, line in enumerate(lines):
    if line == '':
        d = True
        continue
    if d:
        dirList += list(line)
    else:
        map.append(list(line))
        if '@' in line:
            start = (i, line.index('@'))
            map[-1][line.index('@')] = '.'
# for x in map:
#     print(x)
# print(dirList)
# print(start)
for d in dirList:
    # print(d)
    xdir, ydir = dirs[d]
    x, y = start[0] + xdir, start[1] + ydir
    if map[x][y] == '#':
        continue
    elif map[x][y] == '.':
        start = (x,y)
    else:
        spot = (x,y)
        while map[spot[0]][spot[1]] == 'O':
            spot = (spot[0]+xdir, spot[1]+ydir)
            # print(spot, xdir, ydir)
            
        if map[spot[0]][spot[1]] == '.':
            start = (x,y)
            map[x][y], map[spot[0]][spot[1]] = map[spot[0]][spot[1]], map[x][y]

ret = 0
for i, row in enumerate(map):
    for j, ch in enumerate(row):
        if ch == 'O':
            ret += 100 * i + j
print(ret)