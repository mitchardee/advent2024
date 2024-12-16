from collections import Counter, defaultdict, deque
from functools import cache, reduce
from math import inf
from operator import mul


# lines = [x.strip() for x in open("testInput.txt").readlines()]
lines = [x.strip() for x in open("input.txt").readlines()]

dirs = {'^': (-1,0), '<': (0,-1), '>': (0,1), 'v':(1,0)}

d = False
start = None
dirList = []
map = []


for i, line in enumerate(lines):
    if line == '':
        d = True
    elif d:
        dirList += list(line)
    else:
        map.append([])
        for x in line:
            if x == '@':
                start = (i, len(map[-1]))
                map[-1] += ['.', '.']
            elif x == 'O':
                map[-1] += ['[', ']']
            else:
                map[-1] += [x] * 2


for d in dirList:
    xdir, ydir = dirs[d]
    x, y = start[0] + xdir, start[1] + ydir
    if d in ['<', '>']:
        if map[x][y] == '#':
            continue
        elif map[x][y] == '.':
            start = (x,y)
        else:
            spot = (x,y)
            while map[spot[0]][spot[1]] in ['[', ']']:
                spot = (spot[0]+xdir, spot[1]+ydir)
                
            if map[spot[0]][spot[1]] == '.':
                start = (x,y)
                if d == '<':
                    map[x][spot[1]:y] = map[x][spot[1]+1:y+1]
                    map[x][y] = '.'
                else:
                    map[x][y+1:spot[1]+1] = map[x][y:spot[1]]
                    map[x][y] = '.'
    else:
        if map[x][y] == '#':
            continue
        elif map[x][y] == '.':
            start = (x,y)
        else:
            allRocks = []
            moveQ = {(x,y), (x, y + (-1 if map[x][y] == ']' else 1))}
            blocked = False

            while not blocked and moveQ:
                nextQ = set()
                for (i, j) in moveQ:
                    allRocks.append((i,j))
                    nextI = i + xdir
                    ch = map[nextI][j]
                    if ch == '#':
                        blocked = True
                    elif ch == '[':
                        nextQ.add((nextI, j))
                        nextQ.add((nextI, j+1))
                    elif ch == ']':
                        nextQ.add((nextI, j))
                        nextQ.add((nextI, j-1))
                moveQ = nextQ
            
            if not blocked:
                start = (x,y)
                for (i,j) in reversed(allRocks):
                    nextI = i + xdir
                    map[i][j], map[nextI][j] = map[nextI][j], map[i][j]
                    


ret = 0
for i, row in enumerate(map):
    for j, ch in enumerate(row):
        if ch == '[':
            ret += 100 * i + j
print(ret)