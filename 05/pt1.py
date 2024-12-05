from collections import defaultdict

lines = open("input.txt").readlines()
befores, afters = defaultdict(set), defaultdict(set)
j = 0
ret = 0

for i, line in enumerate(lines):
    if '|' not in line:
        j = i+1
        break
    a, b = int(line[:line.index('|')]), int(line[line.index('|')+1:])

    befores[b].add(a)
    afters[a].add(b)


for line in lines[j:]:
    n = [int(x) for x in line.strip().split(',')]
    bad = False
    for i, x in enumerate(n):
        for y in n[i+1:]:
            if y in befores[x]:
                bad = True
    if not bad:
        ret += int(n[len(n)//2])

print(ret)
