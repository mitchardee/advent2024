from collections import Counter, defaultdict, deque
from functools import cache
from heapq import *
from math import inf


# lines = [x.strip() for x in open("testInput.txt").readlines()]
lines = [x.strip() for x in open("input.txt").readlines()]

dirPad = {
    'A': (1,2),
    '^': (1,1),
    '<': (0,0),
    'v': (0,1),
    '>': (0,2),
    (1,2) :'A',
    (1,1) :'^',
    (0,0) :'<',
    (0,1) :'v',
    (0,2) :'>'
}

numPad = {
    'A': (0,2),
    '0': (0,1),
    '1': (1,0),
    '2': (1,1),
    '3': (1,2),
    '4': (2,0),
    '5': (2,1),
    '6': (2,2),
    '7': (3,0),
    '8': (3,1),
    '9': (3,2),
    (0,2) : 'A',
    (0,1) : '0',
    (1,0) : '1',
    (1,1) : '2',
    (1,2) : '3',
    (2,0) : '4',
    (2,1) : '5',
    (2,2) : '6',
    (3,0) : '7',
    (3,1) : '8',
    (3,2) : '9',
}

@cache
def numDirs(a, b):
    dx = numPad[a][1] - numPad[b][1]
    dy = numPad[a][0] - numPad[b][0]
    
    if a == b:
        return ["A"]
    if a == '0' and dx > 0:
        return ['^' + x for x in numDirs('2', b)]
    if a == '1' and dy > 0:
        return ['>' + x for x in numDirs('2', b)]

    ret = []
    if dx > 0:
        ret += ['<' + x for x in numDirs(numPad[(numPad[a][0], numPad[a][1] - 1)], b)]
    if dx < 0:
        ret += ['>' + x for x in numDirs(numPad[(numPad[a][0], numPad[a][1] + 1)], b)]
    if dy < 0:
        ret += ['^' + x for x in numDirs(numPad[(numPad[a][0] + 1, numPad[a][1])], b)]
    if dy > 0:
        ret += ['v' + x for x in numDirs(numPad[(numPad[a][0] - 1, numPad[a][1])], b)]

    return ret

dirDirs = {
    ('A', 'A'): ["A"],
    ('A', '^'): ["<A"],
    ('A', '>'): ["vA"],
    ('A', 'v'): ["<vA", "v<A"],
    ('A', '<'): ["<v<A", "v<<A"],
    ('^', 'A'): [">A"],
    ('^', '^'): ["A"],
    ('^', '>'): ["v>A", ">vA"],
    ('^', 'v'): ["vA"],
    ('^', '<'): ["v<A"],
    ('<', 'A'): [">>^A", ">^>A"],
    ('<', '^'): [">^A"],
    ('<', '>'): [">>A"],
    ('<', 'v'): [">A"],
    ('<', '<'): ["A"],
    ('v', 'A'): [">^A", "^>A"],
    ('v', '^'): ["^A"],
    ('v', '>'): [">A"],
    ('v', 'v'): ["A"],
    ('v', '<'): ["<A"],
    ('>', 'A'): ["^A"],
    ('>', '^'): ["<^A", "^<A"],
    ('>', '>'): ["A"],
    ('>', 'v'): ["<A"],
    ('>', '<'): ["<<A"],
}


@cache
def recDir(a, b, layer):
    if layer == 1:
        # print(dirDirs[(a, b)][0], end='')
        return len(dirDirs[(a, b)][0])#, dirDirs[(a, b)][:1]
    minPath = inf
    bestPath = ""

    for path in dirDirs[(a,b)]:
        prev = 'A'
        pathLen = 0
        # course = [""] * (layer-1)
        
        for x in path:
            t = recDir(prev, x, layer-1)
            pathLen += t#[0]
            # for i, p in enumerate(t[1]):
            #     course[i] += p
            prev = x
        if pathLen < minPath:
            # bestPath = [path] + course
            minPath = pathLen
            bestPath = path

    # print(bestPath, end='')
    return minPath#, ''.join(bestPath)

def numSum(a, b):
    bestSum = inf
    bestPath = ""
    for path in numDirs(a, b):
        prev = 'A'
        s = 0
        for d in path:
            s += recDir(prev, d, 2)
            prev = d
        if bestSum > s:
            bestPath = path
            bestSum = s
    print(bestPath, end='')
    return bestSum
        
# print(numDirs('A', '2'))

ret = 0
prev = 'A'
for line in lines:
    lineSum = 0
    for ch in line:
        inc = numSum(prev, ch)
        lineSum += inc
        prev = ch
    print('\n',lineSum)
    ret += lineSum * int(line[:-1])

print(ret)