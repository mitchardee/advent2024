from collections import defaultdict
from functools import cmp_to_key

lines = open("input.txt").readlines()
afters = defaultdict(set)
j = 0
ret = 0

for i, line in enumerate(lines):
    if '|' not in line:
        j = i+1
        break
    a, b = int(line[:line.index('|')]), int(line[line.index('|')+1:])

    afters[a].add(b)


for line in lines[j:]:
    n = [int(x) for x in line.strip().split(',')]

    if any(
        any(
            x in afters[y] for y in n[i+1:]
            ) 
        for i,x in enumerate(n)
        ):
        n.sort(key=cmp_to_key(
            lambda a, b: 1 if a in afters[b] 
            else -1 if b in afters[a] 
            else 0)
            )
        ret += n[len(n)//2]

print(ret)
