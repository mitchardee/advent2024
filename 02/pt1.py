from collections import defaultdict


lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = [int(x) for x in lines[i].strip().split()]

ret = 0
for line in lines:
    if all(line[i+1] - line[i] in (1,2,3) for i in range(len(line)-1)) or all(line[i] - line[i+1] in (1,2,3) for i in range(len(line)-1)):
        ret += 1

print(ret)


