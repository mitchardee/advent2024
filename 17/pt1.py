from collections import Counter, defaultdict, deque
from heapq import *
from math import inf


# lines = [x.strip().split() for x in open("testInput.txt").readlines()]
lines = [x.strip().split() for x in open("input.txt").readlines()]

regA, regB, regC = int(lines[0][-1]), int(lines[1][-1]), int(lines[2][-1])
prog = [int(x) for x in lines[-1][-1].split(',')]
ins = 0

while 0 <= ins < len(prog):
    op = prog[ins]
    # Unspecified what happens if the instruction pointer tries to read invalid operands
    input = prog[ins+1]
    combo = input
    if input == 4:
        combo = regA
    elif input == 5:
        combo = regB
    elif input == 6:
        combo = regC
    ins += 2

    if op == 0:
        regA >>= combo
    elif op == 1:
        regB ^= input
    elif op == 2:
        regB = combo % 8
    elif op == 3:
        if regA:
            ins = input
    elif op == 4:
        regB ^= regC
    elif op == 5:
        print(combo % 8, end=',')
    elif op == 6:
        regB = regA >> combo
    elif op == 7:
        regC = regA >> combo

print()