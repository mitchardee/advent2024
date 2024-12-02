from collections import defaultdict


lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = [int(x) for x in lines[i].strip().split()]

ret = 0
for l in lines:
    valid = False
    if all(l[i+1] - l[i] in (1,2,3) for i in range(len(l)-1)) or all(l[i] - l[i+1] in (1,2,3) for i in range(len(l)-1)):
        valid = True

    for j in range(len(l)):
        line = l[:j] + l[j+1:]
        if all(line[i+1] - line[i] in (1,2,3) for i in range(len(line)-1)) or all(line[i] - line[i+1] in (1,2,3) for i in range(len(line)-1)):
            valid = True
    ret += bool(valid)

print(ret)


