from collections import defaultdict
from functools import cache

line = [x.strip() for x in open("input.txt").readlines()][0]

tLen = sum(int(x) for x in line)
endLen = sum(int(x) for i, x in enumerate(line) if i%2 == 0)
mem = [None] * tLen
it = 0
for i, ch in enumerate(line):
    if i % 2 == 0:
        for _ in range(int(ch)):
            mem[it] = i//2
            it += 1
    else:
        it += int(ch)

l, r = 0, tLen-1

while l < r:
    if mem[l] != None or mem[r] == None:
        if mem[l] != None:
            l += 1
        if mem[r] == None:
            r -= 1
    else:
        mem[r], mem[l] = mem[l], mem[r]

ret = 0
for i in range(endLen):
    ret += i * mem[i]
print(ret)
