from collections import Counter, defaultdict, deque
from heapq import *
from math import inf


# lines = [x.strip().split() for x in open("testInput.txt").readlines()]
lines = [x.strip().split() for x in open("input.txt").readlines()]

prog = [int(x) for x in lines[-1][-1].split(',')]


def op(a):
    b = a%8
    c = a >> (b^1)
    b ^= 4 ^ c
    return b%8

def dfs(i, a):
    if i < 0:
        print(a)
        return True
    else:
        for x in range(8):
            if prog[i] == op(a * 8 + x):
                if dfs(i-1, a * 8 + x):
                    return True
        return False

dfs(len(prog)-1, 0)