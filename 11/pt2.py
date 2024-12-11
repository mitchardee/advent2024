from collections import defaultdict
from functools import cache

line = [[int(k) for k in x.strip().split()] for x in open("input.txt").readlines()][0]

@cache
def stones(inX, reps):
    if reps == 0:
        return 1
    if inX == 0:
        return stones(1, reps - 1)
    elif (l := (len(s := str(inX)))) % 2 == 0:
        return stones(int(s[:l//2]), reps - 1) + stones(int(s[l//2:]), reps - 1)
    else:
        return stones(inX * 2024, reps - 1)

print(sum(stones(x, 75) for x in line))