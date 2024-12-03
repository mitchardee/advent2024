line = ''.join(open("input.txt").readlines())
ret = 0

for i in range(len(line)):
    if line[i:i+4] == "mul(":
        if ')' in line[i+7:i+12]:
            close = line[i+7:i+12].index(')')
            subS = line[i+4:i+7+close]

            if ',' in subS[1:-1]:
                comma = subS[1:-1].index(',') + 1
                if subS[:comma].isdigit() and subS[comma+1:].isdigit():
                    ret += int(subS[:comma]) * int(subS[comma+1:])

print(ret)