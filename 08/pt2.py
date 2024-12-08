from collections import defaultdict
from functools import cache

lines = [x.strip() for x in open("input.txt").readlines()]

nodes = defaultdict(list)
ants = set()
r, c = len(lines), len(lines[0])

for i, line in enumerate(lines):
    for j, x in enumerate(line):
        if x != '.':
            nodes[x].append((i, j))

for k, v in nodes.items():
    for i, a in enumerate(v):
        for j, b in enumerate(v[i+1:]):
            diff = (a[0] - b[0], a[1] - b[1])
            newA = a
            while 0 <= newA[0] < r and 0 <= newA[1] < c:
                ants.add(newA)
                newA = (newA[0] + diff[0], newA[1] + diff[1])
            newB = b
            while 0 <= newB[0] < r and 0 <= newB[1] < c:
                ants.add(newB)
                newB = (newB[0] - diff[0], newB[1] - diff[1])

print(len(ants))