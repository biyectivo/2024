import re
import math
import numpy as np
import itertools as it
import time

grid = []
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_11.txt") as file:
    grid = file.readline().split()
original_grid = grid.copy()

#part 1
#naive approach
def blink():
    global grid
    new = []
    for i in range(0,len(grid)):
        if grid[i] == str(0):
            new.append(str(1))
        elif len(grid[i]) % 2 == 0:
            left = str(int(grid[i][0:len(grid[i])//2]))
            right = str(int(grid[i][len(grid[i])//2:len(grid[i])]))
            new.append(left)
            new.append(right)
        else:
            new.append(str(int(grid[i])*2024))
    grid = new
    print(len(grid), grid)

t = time.time()
print(grid)

unique  = set()
for i in range(0,25):
    blink()
    
print(f"Total: {len(grid)}")
print(f"Grid: {grid}")


# part 2
counts = {}

print("~~~~~~~~~~~~~~~~~~~")
print("Part 2")

def blink_stone(s):
    if s == str(0):
        return str(1)
    elif len(s) % 2 == 0:
        left = str(int(s[0:len(s)//2]))
        right = str(int(s[len(s)//2:len(s)]))
        return (left,right)
    else:
        return str(int(s)*2024)
        
t = time.time()
#print(grid)

# add initial counts
grid = original_grid
for g in grid:
    if g in counts.keys():
        counts[g] += 1
    else:
        counts[g] = 1

#print(counts)
#print(grid)

# process blink

for w in range(0,75):
    old_counts = counts.copy()
    for g in old_counts.keys():
        n = old_counts[g]
        #print(g,counts[g])
        counts[g] -= n
        if counts[g] == 0:
            counts.pop(g, None)
        
        x = blink_stone(g)
        if type(x) is tuple:
            if x[0] in counts.keys():
                counts[x[0]] += n
            else:
                counts[x[0]] = n
            if x[1] in counts.keys():
                counts[x[1]] += n
            else:
                counts[x[1]] = n
        else:
            if x in counts.keys():
                counts[x] += n
            else:
                counts[x] = n
            #print(f"  after g: {counts}")
    #print(w,old_counts)
    #print(w,counts)
    
total = 0
for k in counts.keys():
    total += counts[k]

print(total)

print(f"Time: {time.time()-t} seconds")