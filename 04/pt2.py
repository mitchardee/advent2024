
lines = [list(x.strip()) for x in open("input.txt").readlines()]
ret = 0

for i, line in enumerate(lines[1:-1], 1):
    for j, x in enumerate(line[1:-1], 1):
        if x == 'A':
            if sorted([lines[i-1][j-1], lines[i+1][j+1]]) == sorted([lines[i+1][j-1], lines[i-1][j+1]]) == ['M','S']:
                ret += 1

print(ret)
