from math import inf

lines = [x.split() for x in open("input.txt").readlines()]
tups = []
ret = 0

for i in range(0, len(lines), 4):
    tups.append(tuple(int (x) for x in (
        lines[i][2][2:-1], 
        lines[i][3][2:], 
        lines[i+1][2][2:-1], 
        lines[i+1][3][2:], 
        10000000000000 + int(lines[i+2][1][2:-1]), 
        10000000000000 + int(lines[i+2][2][2:])
        )))


for i, (ax, ay, bx, by, tx, ty) in enumerate(tups):   
    swapped = False
    if ax < ay:
        swapped = True
        ax, ay, bx, by = bx, by, ax, ay

    # Can't make the needed combo unless one ratio is bigger and one smaller (impossible to be equal)
    if ax < ay:
        continue

    # Binary search for the number of A presses?
    l, r = 0, tx + 1
    while l + 1 < r:
        a = (l+r)//2
        if a * ax > tx or a * ay > ty:
            r = a
        else:
            xd, yd = tx - a * ax, ty - a * ay
            
            det = bx * yd - by * xd
            #Found the correct ratio
            if det == 0:
                l = r = a
            # xd is too big compared to yd
            elif det < 0:
                l = a
            else:
                r = a

    if l == r:
        a = l
        b = (tx - a * ax) // bx
        if a * ax + b * bx == tx and a * ay + b * by == ty:
            ret += a + b + 2 * (b if swapped else a)

print(ret)