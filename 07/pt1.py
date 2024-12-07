from collections import defaultdict
from functools import cache

lines = [x.strip().split() for x in open("testInput.txt").readlines()]
targets = [int(line[0][:-1]) for line in lines]
operands = [[int(x) for x in line[1:]] for line in lines]
ret = 0

@cache
def outs(lineNum, i):
    if i >= len(operands[lineNum]) - 1:
        return {operands[lineNum][0]}
    return {
        (operands[lineNum][-1-i] + x) 
        for x in outs(lineNum, i+1) 
        if (operands[lineNum][-1-i] + x) <= targets[lineNum]
    } | {
        (operands[lineNum][-1-i] * x) 
        for x in outs(lineNum, i+1) 
        if (operands[lineNum][-1-i] + x) <= targets[lineNum]
    }

for i in range(len(lines)):
    if targets[i] in outs(i, 0):
        ret += targets[i]

print(ret)