
lines = [list(x.strip()) for x in open("input.txt").readlines()]
dirs = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
dirs3 = ((-3,-3),(-3,0),(-3,3),(0,-3),(0,3),(3,-3),(3,0),(3,3))
ret = 0

for i, line in enumerate(lines):
    for j, x in enumerate(line):
        if x == 'X':
            for d in range(8):
                if 0 <= i + dirs3[d][0] < len(lines) and 0 <= j + dirs3[d][1] < len(line):
                    if (lines[i + dirs[d][0]][j + dirs[d][1]] == 'M' and
                        lines[i + 2*dirs[d][0]][j + 2*dirs[d][1]] == 'A' and
                        lines[i + 3*dirs[d][0]][j + 3*dirs[d][1]] == 'S'):
                        ret += 1

print(ret)
