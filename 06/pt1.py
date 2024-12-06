from collections import defaultdict

lines = [x.strip() for x in open("input.txt").readlines()]
obs = set()
pos = (0,0)
dirs = ((-1,0),(0,1),(1,0),(0,-1))
d = 0
entered = set()

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        match ch:
            case '^':
                pos = (i,j)
            case '#':
                obs.add((i, j))


while 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0]):
    entered.add(pos)
    nex = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
    # print("nex:", nex)
    if nex in obs:
        d = (d+1) % 4
    else:
        pos = nex

# for i in range(len(lines)):
#     for j in range(len(lines[0])):
#         print('#' if lines[i][j] == '#' else 'X' if (i,j) in entered else '.', end='')
#     print()

print(len(entered))