from collections import Counter, defaultdict, deque
from functools import cache, reduce
from math import inf
from operator import mul

# lines = [x.strip().split() for x in open("testInput.txt").readlines()]
# r, c, steps = 11, 7, 100
lines = [x.strip().split() for x in open("input.txt").readlines()]
r, c, steps = 101, 103, 100

quads = [0] * 4
map = Counter()

for i, line in enumerate(lines):
    t1, t2 = line[0].split(','), line[1].split(',')
    lines[i] = [int(x) for x in (t1[0][2:], t1[1], t2[0][2:], t2[1])]

for (x, y, dx, dy) in lines:
    x, y = (x + steps * dx) % r, (y + steps * dy) % c
    map[(x, y)] += 1
    if x < r // 2:
        if y < c // 2:
            quads[0] += 1
        elif y > c // 2:
            quads[1] += 1
    elif x > r // 2:
        if y < c // 2:
            quads[2] += 1
        elif y > c // 2:
            quads[3] += 1

# for j in range(c):
#     for i in range(r):
#         print('.' if (i,j) not in map else map[(i,j)], sep=None, end='')
#     print()

print(reduce(mul, quads, 1))