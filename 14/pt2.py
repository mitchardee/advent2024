from collections import Counter, defaultdict, deque
from functools import cache, reduce
from math import inf
from operator import mul

# lines = [x.strip().split() for x in open("testInput.txt").readlines()]
# r, c, steps = 11, 7, 101
lines = [x.strip().split() for x in open("input.txt").readlines()]
r, c, steps = 101, 103, 10000
dirs = ((-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))


for i, line in enumerate(lines):
    t1, t2 = line[0].split(','), line[1].split(',')
    lines[i] = [int(x) for x in (t1[0][2:], t1[1], t2[0][2:], t2[1])]

for s in range(1, steps):
    map = Counter()

    for i, (x, y, dx, dy) in enumerate(lines):
        x, y = (x + dx) % r, (y + dy) % c
        map[(x, y)] += 1
        lines[i][0], lines[i][1] = x, y

    # print(quads)
    # print(centrality, dangerSum / s)
    if any(all((x+i, y) in map for i in range(8)) for (x,y,_,_) in lines):

        print('\n', s)
        for j in range(c):
            for i in range(r):
                print(' ' if (i,j) not in map else map[(i,j)], sep=None, end='')
            print()
