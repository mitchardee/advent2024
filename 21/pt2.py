from functools import cache
from math import inf


# lines = [x.strip() for x in open("testInput.txt").readlines()]
lines = [x.strip() for x in open("input.txt").readlines()]

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
        return len(dirDirs[(a, b)][0])
    
    minPath = inf

    for path in dirDirs[(a,b)]:
        path = 'A' + path
        minPath = min(
            minPath, 
            sum(
                recDir(path[i], path[i+1], layer-1) for i in range(len(path)-1)
            )
        )

    return minPath

def numSum(a, b):
    bestSum = inf
    for path in numDirs(a, b):
        path = 'A' + path
        bestSum = min(
            bestSum, 
            sum(
                recDir(path[i], path[i+1], 25) for i in range(len(path)-1)
            )
        )

    return bestSum
        

ret = 0
prev = 'A'
for line in lines:
    lineSum = 0
    for ch in line:
        inc = numSum(prev, ch)
        lineSum += inc
        prev = ch
    ret += lineSum * int(line[:-1])

print(ret)