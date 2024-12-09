from heapq import *

line = [x.strip() for x in open("input.txt").readlines()][0]

tLen = sum(int(x) for x in line)
mem = [0] * tLen
# Make a list of heaps of locations with a given length of free space
frees = [[] for _ in range(10)]

it = 0
for i, ch in enumerate(line):
    if i % 2 == 0:
        for _ in range(int(ch)):
            mem[it] = i//2
            it += 1
    else:
        frees[int(ch)].append(it)
        it += int(ch)


r = tLen
for i, ch in reversed(list(enumerate(line))):
    # Move r pointer to the beginning of the block
    r -= (x := int(ch))

    # If this is a data block
    if i % 2 == 0:
        for j in range(x, 10):
            # Clear out any heaps without low-enough memory addresses
            if frees[j] and frees[j][0] >= r:
                frees[j].clear()
        
        # Find the earliest available spot with enough contiguous free memory
        j = min((k for k in range(x, 10) if frees[k]), key=lambda k: frees[k][0], default=None)
        if j:
            # Swap the free memory values with the data block
            l = heappop(frees[j])
            heappush(frees[j-x], l+x)
            for k in range(x):
                mem[l + k], mem[r + k] = mem[r + k], mem[l + k]
    

print(sum(i * x for i, x in enumerate(mem)))
