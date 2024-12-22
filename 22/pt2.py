from functools import cache

# lines = [int(x.strip()) for x in open("testInput.txt").readlines()]
lines = [int(x.strip()) for x in open("input.txt").readlines()]

prices = [{} for _ in range(len(lines))]
def op(x):
    x = (x ^ (x << 6)) % 16777216
    x = (x ^ (x >> 5)) % 16777216
    x = (x ^ (x << 11)) % 16777216
    return x

for i, x in enumerate(lines):
    l = []
    for _ in range(3):
        nex = op(x)
        l.append((nex%10) - (x%10))
        x = op(x)
    for j in range(2000-3):
        nex = op(x)
        l.append((nex%10) - (x%10))
        x = nex
        t = tuple(l[-4:])
        if t not in prices[i]:
            prices[i][t] = x%10

allSeqs = set()
for p in prices:
    allSeqs |= set(p.keys())

bestYet = 0
bestT = ()
for t in allSeqs:
    tot = 0
    for p in prices:
        if t in p:
            tot += p[t]
    if bestYet < tot:
        bestYet = tot
        bestT = t

print(bestYet, bestT)
