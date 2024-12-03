import re

line = ''.join(open("testInput.txt").readlines())
ret = 0

phrases = re.findall('mul\(\d\d?\d?,\d\d?\d?\)', line)
for x in phrases:
    ret += int(x[4:x.index(',')]) * int(x[x.index(',')+1:-1])

print(ret)
