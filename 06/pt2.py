from collections import defaultdict

lines = [x.strip() for x in open("input.txt").readlines()]
obs = set()
dirs = ((-1,0),(0,1),(1,0),(0,-1))
ret = 0

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        match ch:
            case '^':
                start = (i,j)
            case '#':
                obs.add((i, j))


for i in range(len(lines)):
    for j in range(len(lines[0])):
        if (i, j) not in obs and (i,j) != start:
            obs.add((i, j))
            pos = (start[0], start[1], 0)
            entered = set()
            while 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0]):
                if pos in entered:
                    ret += 1
                    break
                entered.add(pos)
                nex = (pos[0] + dirs[pos[2]][0], pos[1] + dirs[pos[2]][1])
                if nex in obs:
                    pos = (pos[0], pos[1], (pos[2]+1)%4)
                else:
                    pos = (nex[0], nex[1], pos[2])
            obs.remove((i, j))


print(ret)