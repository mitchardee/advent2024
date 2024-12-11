from collections import defaultdict
from functools import cache

line = [[int(k) for k in x.strip().split()] for x in open("input.txt").readlines()][0]
nextLine = []

for k in range(25):
    for x in line:
        if x == 0:
            nextLine.append(1)
        elif (l := (len(s := str(x)))) % 2 == 0:
            nextLine.append(int(s[:l//2]))
            nextLine.append(int(s[l//2:]))
        else:
            nextLine.append(x * 2024)
    line, nextLine = nextLine, []
    # print(k, len(line), line)
print(len(line))