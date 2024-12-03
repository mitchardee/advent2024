import re

line = ''.join(open("input.txt").readlines())
ret = 0
enabledBit = 1

phrases = re.findall(r'(mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\)){1}', line)
for x in phrases:
    match x:
        case "do()":
            enabledBit = 1
        case "don't()":
            enabledBit = 0
        case default:
            ret += int(x[4:x.index(',')]) * int(x[x.index(',')+1:-1]) * enabledBit


print(ret)